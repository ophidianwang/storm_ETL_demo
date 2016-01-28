#!/bin/bash
cd $(dirname $0)

srv04=vagrant@172.28.128.22 # localhost; this script should run on it
srv05=vagrant@172.28.128.23
srv06=vagrant@172.28.128.24

# clear dir content
rm  /home/vagrant/source/*
ssh $srv05 "rm /home/vagrant/source/*"
ssh $srv06 "rm /home/vagrant/source/*"

sleep 2

# copy raw file
cp lte_pgw/CGW11_pgw_processed_01_201511050* /home/vagrant/source
scp lte_pgw/CGW11_pgw_processed_01_201511051* $srv05:/home/vagrant/source
scp lte_pgw/CGW11_pgw_processed_01_201511052* $srv06:/home/vagrant/source
