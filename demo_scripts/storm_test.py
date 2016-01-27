# -*- coding: utf-8 -*-

import time
from datetime import datetime
import subprocess
from pymongo import MongoClient

client = MongoClient('172.28.128.22', 40000)
db = client.cep_storm
collection = db.lte_pgw_exp

topology_path = "/home/vagrant/petrel_exp2/"
submit_sh = topology_path + "cluster_run.sh"
kill_sh = topology_path + "cluster_kill.sh"
kill_all_sh = topology_path + "kill_GenericTopology.sh"

# kill topology
subprocess.call(["bash", kill_sh])
time.sleep(25)
subprocess.call(["bash", kill_all_sh])
time.sleep(5)
# to make sure topology is over
print("kill topology done at {0}.".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# clear mongodb records
collection.delete_many({})
print("clear collection done at {0}.".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
check_count = collection.count()
if check_count != 0:
    print("error happened, collection.count() is not 0")
    raise SystemExit("mongodb error")

# start topology
subprocess.call(["bash", submit_sh])
print("submit topology done at {0}.".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
time.sleep(5)  # topology deploying
print("start monitoring mongodb at {0}.".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# then check mongodb, out input data should be remodeled from 1085420 to 570720
row_count = 0
row_progress = 0
dump_start_timestamp = 0
over_counter = 0
diff_threshold = 1000
tolerance_count = 300
sleep_time = 0.1
tolerance_time = tolerance_count * sleep_time
while True:
    row_count = collection.count()  # get current row count
    if dump_start_timestamp == 0 and row_count != 0:
        dump_start_timestamp = time.time()  # mark timestamp which means start writing
    diff = row_count - row_progress
    if diff > 1000:
        print("There are {0} records in mongodb now.".format(row_count))
        row_progress = row_count
        over_counter = 0
    elif row_count != 0:
        over_counter += 1
        if over_counter > 50:
            print("over_counter: {0}".format(over_counter))

    if over_counter >= tolerance_count:
        break
    time.sleep(sleep_time)  # in case too many queries affect mongodb performance...

dump_end_timestamp = time.time() - tolerance_time

log_path = "/realtime/storm_log/storm_petrel_{0}_{1}.log"
today = datetime.now().strftime("%Y%m%d")
spout_log_path = log_path.format("ExpSpout", today)

consume_start_timestamp = 0
consume_end_timestamp = 0
emit_end_timestamp = 0
with open(spout_log_path, "r") as f:
    for line in f:
        line = line.strip()
        if line.find("start") != -1:
            consume_start_timestamp = float(line.split(" ")[-2])
        elif line.find("finish") != -1:
            consume_end_timestamp = float(line.split(" ")[-2])
        elif line.find("emit") != -1:
            emit_end_timestamp = float(line.split(" ")[-2])

raw_count = 1000000

print("Spout start consuming {0} records at {1}".format(raw_count,
                                                        datetime.fromtimestamp(consume_start_timestamp).strftime(
                                                                "%Y-%m-%d %H:%M:%S")))
print("Spout finish consuming {0} records at {1}".format(raw_count,
                                                         datetime.fromtimestamp(consume_end_timestamp).strftime(
                                                                 "%Y-%m-%d %H:%M:%S")))
print("Spout finish emit {0} tuples at {1}".format(raw_count, datetime.fromtimestamp(emit_end_timestamp).strftime(
        "%Y-%m-%d %H:%M:%S")))
print("Bolt start dumping {0} records at {1}".format(raw_count, datetime.fromtimestamp(dump_start_timestamp).strftime(
        "%Y-%m-%d %H:%M:%S")))
print("Bolt finish dumping {0} records at {1}".format(raw_count, datetime.fromtimestamp(dump_end_timestamp).strftime(
        "%Y-%m-%d %H:%M:%S")))
print("===")
print("{0} records".format(row_count))
print(
    "Spout spend {0} seconds consuming {1} messages".format(consume_end_timestamp - consume_start_timestamp, raw_count))
print("Spout spend {0} seconds emitting {1} tuples".format(emit_end_timestamp - consume_start_timestamp, raw_count))
print("Bolt spend {0} seconds dumping {1} records.".format(dump_end_timestamp - dump_start_timestamp, raw_count))
print("The 1th record walks through the topology in {1} seconds".format(raw_count,
                                                                        dump_start_timestamp - consume_start_timestamp))
print("The {0}th record walks through the topology in {1} seconds".format(raw_count,
                                                                          dump_end_timestamp - consume_end_timestamp))
