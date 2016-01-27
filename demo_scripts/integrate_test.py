# -*- coding: utf-8 -*-

import time
from datetime import datetime
import subprocess
import uuid
from pymongo import MongoClient
import paramiko
import os
import random

start_timestamp = 0
end_timestamp = 0

raw_count = 100000  # 100000 1085420
target_count = 37397  # 37397 570000
client = MongoClient('172.28.128.22', 40000)
db = client.cep_storm
collection = db.lte_pgw_exp

# fluentd, kafka, mongodb, storm-topology suppose needs to be running

# clear mongodb records
collection.delete_many({})

hosts = ["localhost", "172.28.128.23", "172.28.128.24"]
clients = []
sftps = []

for cursor, host in enumerate(hosts):
    if host == "localhost":
        clients.append(None)
        sftps.append(None)
        continue
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hosts[cursor], username="vagrant", password="vagrant")  # to remote hosts
    sftp = client.open_sftp()
    clients.append(client)
    sftps.append(sftp)

print("%s", clients)
print("%s", sftps)

start_timestamp = time.time()

# cp/scp file for fluentd parsing

dest_dir = "/home/vagrant/source/"
original_dir = "/home/vagrant/source_split/"
files = os.listdir(original_dir)
for cursor, filename in enumerate(files):
    original_file = original_dir + filename
    current = cursor % 3
    dest_file = dest_dir + uuid.uuid4().hex
    print("from %s to %s", original_file, dest_file)
    if current == 0:
        subprocess.call(["cp", original_file, dest_file])
    else:
        sftps[current].put(original_file, dest_file)
"""
dest_file = "/home/vagrant/source/" + uuid.uuid4().hex
subprocess.call(["cp", "/home/vagrant/source/CGW11_pgw_processed_01_20151105020743.cdr.gz.csv", dest_file])
"""

# then check mongodb, out input data should be remodeled from 100000 to 37397 / 1085420 to 570720
row_count = 0
row_progress = 0
dump_timestamp = 0
while True:
    row_count = collection.count()  # get current row count
    if dump_timestamp == 0 and row_count != 0:
        dump_timestamp = time.time()  # mark timestamp which means start writing
    diff = row_count - row_progress
    if diff > 1000:
        print("There are {0} records in mongodb now.".format(row_count))
        row_progress = row_count
    # end loop when no more documents are writen to mongodb
    if row_count >= target_count:
        end_timestamp = time.time()
        break
    time.sleep(0.3)  # in case query affect mongodb performance...

end_timestamp = time.time()

log_path = "/realtime/storm_log/storm_petrel_{0}_{1}.log"
today = datetime.now().strftime("%Y%m%d")
spout_log_path = log_path.format("ExpSpout", today)

get_all_msg_timestamp = 0
with open(spout_log_path, "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            get_all_msg_timestamp = float(line.split(" ")[-2])  # get the last line

print(
    "ETL start at {0} , {1}".format(start_timestamp,
                                    datetime.fromtimestamp(start_timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print("Storm Spout get all message from kafka {0} , {1}".format(get_all_msg_timestamp,
                                                                datetime.fromtimestamp(get_all_msg_timestamp).strftime(
                                                                        "%Y-%m-%d %H:%M:%S")))
print("Storm Bolt start dumping to mongodb at {0} , {1}".format(dump_timestamp,
                                                                datetime.fromtimestamp(dump_timestamp).strftime(
                                                                        "%Y-%m-%d %H:%M:%S")))
print("ETL end at {0} , {1}".format(end_timestamp, datetime.fromtimestamp(end_timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print(
    "(fluentd, kafka, spout) spend {0} seconds processing {1} records.".format(get_all_msg_timestamp - start_timestamp,
                                                                               raw_count))
print("realtime lag of storm is {0} seconds".format(dump_timestamp - get_all_msg_timestamp))
print("(bolt, mongodb) spend {0} seconds processing {1} records.".format(end_timestamp - dump_timestamp, raw_count))
print("ETL spend {0} seconds processing {1} records.".format(end_timestamp - start_timestamp, raw_count))
