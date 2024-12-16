#!/bin/sh
newman run Peer2Peer_API.postman_collection.json -d test_cases.csv -e test_environment.postman_environment.json --verbose 2>&1 | tee -i -a "output.log"