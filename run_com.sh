#!/bin/sh
# Argument: image id of your server image
serverImageId=$1
ip=172.99.0.3
docker run --net custom-net --ip $ip $serverImageId