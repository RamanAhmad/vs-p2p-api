#!/bin/sh
port=$1
./broadcast/run.sh $port
environment="broadcast/test_environment.postman_environment.json"
python3 testcases/TestGenerator.py $environment