#!/bin/bash
source ~/petrel_env/bin/activate
cd $(dirname $0)
python demo_scripts/storm_test.py
