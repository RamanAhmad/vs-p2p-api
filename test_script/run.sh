#!/bin/sh
PORT=$1
BROADCAST_ADDR=$2
TEST_SUB=$3
ENVIRONMENT_FILE=$4
python3 broadcast/src/broadcast_to_postman_environment.py $BROADCAST_ADDR $PORT
python3 testcases/TestGenerator.py $ENVIRONMENT_FILE $TEST_SUB
newman run p2p-postman-collection/Peer2Peer_API.postman_collection.json \
    -d out/test_cases/test_cases.csv \
    -e $ENVIRONMENT_FILE \
    --timeout-request 500\
    -r htmlextra \
    --verbose 2>&1 | tee -i -a "output.log"