# -*- coding: utf-8 -*-

import os
from pykafka import KafkaClient

original_dir = "/home/vagrant/lte_pgw/"
files = os.listdir(original_dir)
print(files)

client = KafkaClient(hosts='172.28.128.22:9092,172.28.128.23:9092,172.28.128.24:9092')
print(client.topics)

# 取得指定的kafka_topic物件
topic = client.topics['cep_storm']

with topic.get_producer(delivery_reports=True) as producer:
    # for file in target dir
    # produce message averagely to two topic
    message_cursor = 0
    for file_order, filename in enumerate(files):
        source_file = original_dir + filename
        # produce messages
        with open(source_file, "r") as f:
            for line in f:
                message_cursor += 1
                producer.produce('message:{0}'.format(line.strip()), partition_key='{}'.format(message_cursor))

        print("file: {0} , produce to kafka topic: cep_storm done.".format(filename))
        print("current message #: {0}".format(message_cursor))

print("all file to kafka done.")
