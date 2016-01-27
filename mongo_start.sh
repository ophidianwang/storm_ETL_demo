#!/bin/bash

#1. directory 建立 

# dip-bd01  $s1 $c1 $m1
s1=/data/db/s1
c1=/data/db/c1
m1=/data/db/m1

# dip-bd02  $s2 $c2 $m2
s2=/data/db/s2
c2=/data/db/c2
m2=/data/db/m2

# dip-bd03  $s3 $c3 $m3
s3=/data/db/s3
c3=/data/db/c3
m3=/data/db/m3


# hostname 對應IP
bd04=172.28.128.22
bd05=172.28.128.23
bd06=172.28.128.24


srv04=vagrant@172.28.128.22
srv05=vagrant@172.28.128.23
srv06=vagrant@172.28.128.24



#2. mongod 啟動
# 若有 NUMA 問題 ，改用 numactl --interleave=all 開頭
ssh $srv04 "mongod --quiet --port 20001 --dbpath $s1 --logpath $s1/s1.log --replSet sh01 --shardsvr --directoryperdb --fork --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy"

ssh $srv05 "mongod --quiet --port 20002 --dbpath $s2 --logpath $s2/s2.log --replSet sh02 --shardsvr --directoryperdb --fork --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy"

ssh $srv06 "mongod --quiet --port 20003 --dbpath $s3 --logpath $s3/s3.log --replSet sh03 --shardsvr --directoryperdb --fork --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy"

ssh $srv04 "mongod --quiet --configsvr --dbpath $c1 --logpath $c1/c1.log --port 30001 --fork --directoryperdb --nojournal --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy "

ssh $srv05 "mongod --quiet --configsvr --dbpath $c2 --logpath $c2/c2.log --port 30002 --fork --directoryperdb --nojournal --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy "

ssh $srv06 "mongod --quiet --configsvr --dbpath $c3 --logpath $c3/c3.log --port 30003 --fork --directoryperdb --nojournal --storageEngine wiredTiger --wiredTigerCollectionBlockCompressor snappy"


ssh $srv04 "mongos --port 40000 --configdb $bd04:30001,$bd05:30002,$bd06:30003 --logpath $m1/mos.log --fork"
ssh $srv05 "mongos --port 40000 --configdb $bd04:30001,$bd05:30002,$bd06:30003 --logpath $m2/mos.log --fork"
ssh $srv06 "mongos --port 40000 --configdb $bd04:30001,$bd05:30002,$bd06:30003 --logpath $m3/mos.log --fork"
