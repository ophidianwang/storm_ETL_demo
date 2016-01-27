#!/bin/bash
cd $(dirname $0)
nohup sudo python log_listener.py &
