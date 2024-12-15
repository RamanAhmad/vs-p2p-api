#!/bin/sh
newman run Peer2Peer_API_Collection.json -d test_cases.csv -e test_environment.postman_environment.json 2>&1 | tee -i "output.log"