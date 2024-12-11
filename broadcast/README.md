# Prerequisites

1. Your server app runs in a docker container
2. Your server app answers to udp brodcast on a specified port with a json readable string

# Manual

## Setup resources (optional for newest environment file)
1. export environment of postman collection from https://vs-starteam.postman.co/workspace/Team-Workspace~01d6b382-1387-40ea-8495-538c2634f4a0/overview

2. copy file to resources/

3. rename to test_environment.postman_environment.json

## Run Script
1. run
    ```
    .\run.sh <udp-port>
    ```
HINT: If operating on windows use cygwin or git bash terminal.
