#!/bin/bash

srv04=vagrant@172.28.128.22 # localhost; this script should run on it
srv05=vagrant@172.28.128.23
srv06=vagrant@172.28.128.24

sudo apt-get install -y python-virtualenv
ssh $srv05 "sudo apt-get install -y python-virtualenv"
ssh $srv06 "sudo apt-get install -y python-virtualenv"

cd ~
virtualenv --always-copy petrel_env
deactivate
source ~/petrel_env/bin/activate
easy_install petrel==0.9.4.0.3
pip install -U pip
pip install pykafka==2.1.2 pymongo==3.2
