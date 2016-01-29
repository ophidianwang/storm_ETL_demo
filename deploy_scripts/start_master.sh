#!/bin/bash
cd /home/vagrant
/realtime/zookeeper-3.4.7/bin/zkServer.sh start &
sleep 7
/realtime/kafka_2.11-0.8.2.2/bin/kafka-server-start.sh /home/vagrant/kafka-server.properties &
sleep 5
/home/vagrant/fluentd_start.sh &
sleep 3
/realtime/apache-storm-0.9.4/bin/storm nimbus &
/realtime/apache-storm-0.9.4/bin/storm ui &
/realtime/apache-storm-0.9.4/bin/storm supervisor &


