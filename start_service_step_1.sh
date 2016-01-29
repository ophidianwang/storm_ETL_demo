#!/bin/bash
# start fluentd, zookeeper, kafka, storm, mongodb; prepare some dir for demo
# start log listener; distribute raw file to all host

cd $(dirname $0)

srv04=vagrant@172.28.128.22 # localhost; this script should run on it
srv05=vagrant@172.28.128.23
srv06=vagrant@172.28.128.24

# make / clear the dir which fluentd instances listen to
rm  -r /home/vagrant/source
ssh $srv05 "rm -r /home/vagrant/source"
ssh $srv06 "rm -r /home/vagrant/source"
sleep 1
mkdir /home/vagrant/source
ssh $srv05 "mkdir /home/vagrant/source"
ssh $srv06 "mkdir /home/vagrant/source"

# copy kafka-server.properties
cp kafka-properties/server-z3-b5-p3.properties /home/vagrant/kafka-server.properties
scp kafka-properties/server-z3-b6-p3.properties $srv05:/home/vagrant/kafka-server.properties
scp kafka-properties/server-z3-b7-p3.properties $srv06:/home/vagrant/kafka-server.properties

# copy service script
cp deploy_scripts/start_master.sh /home/vagrant/start_master.sh
scp deploy_scripts/start_slave.sh $srv05:/home/vagrant/start_slave.sh
scp deploy_scripts/start_slave.sh $srv06:/home/vagrant/start_slave.sh

echo "starting service step1 done."