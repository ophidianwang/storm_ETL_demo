# -*- coding: utf-8 -*-

from datetime import datetime

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
print("Spout start consuming {0} records at {1}".format(raw_count, datetime.fromtimestamp(consume_start_timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print("Spout finish consuming {0} records at {1}".format(raw_count, datetime.fromtimestamp(consume_end_timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print("Spout finish emit {0} tuples at {1}".format(raw_count, datetime.fromtimestamp(emit_end_timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print("===")
print("Spout spend {0} seconds consuming {1} messages".format(consume_end_timestamp - consume_start_timestamp, raw_count))
print("Spout spend {0} seconds emitting {1} tuples".format(emit_end_timestamp - consume_start_timestamp, raw_count))