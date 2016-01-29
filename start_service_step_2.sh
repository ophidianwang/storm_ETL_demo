#!/bin/bash
# start fluentd, zookeeper, kafka, storm, mongodb; prepare some dir for demo
# start log listener; distribute raw file to all host

cd $(dirname $0)

srv04=vagrant@172.28.128.22 # localhost; this script should run on it
srv05=vagrant@172.28.128.23
srv06=vagrant@172.28.128.24

/realtime/kafka_2.11-0.8.2.2/bin/kafka-topics.sh --delete --zookeeper 172.28.128.22:2181,172.28.128.23:2181,172.28.128.24:2181 --topic cep_storm
sleep 3
/realtime/kafka_2.11-0.8.2.2/bin/kafka-topics.sh --create --zookeeper 172.28.128.22:2181,172.28.128.23:2181,172.28.128.24:2181 --partitions 3 --replication-factor 3 --topic cep_storm
sleep 3

# manual start kafka-manger with password
nohup ssh $srv06  "sudo /home/vagrant/kafka-manager-1.3.0.4/bin/kafka-manager -Dconfig.file=/home/vagrant/kafka-manager-1.3.0.4/conf/application.conf -Dhttp.port=9001" &

# kill existing topology
source /home/vagrant/petrel_env/bin/activate
./topology/cluster_kill.sh

sleep 10

# start mongo on all host
./mongo_start.sh &

# start log_listener on srv04
./log_listener/run.sh &
# nohup sudo python /home/vagrant/log_listener/log_listener.py & # manual start with password

# distribute files to all host (dir. that fluentd listen to)
./distribute_file.sh

echo "starting service step2 done."