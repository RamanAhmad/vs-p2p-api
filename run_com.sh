#!/bin/sh
# Argument: image id of your server image
serverImageId=$1
ip=$2
docker run --net custom-net --ip $ip $serverImageId