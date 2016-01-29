#!/bin/bash
cd $(dirname $0)
source ~/petrel_env/bin/activate
python demo_scripts/kafka_check.py
