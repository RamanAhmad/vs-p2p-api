#!/bin/sh
# Author : Ansgar Deuschel
udpPort="$1"
broadcast_address=$2
ip=$3
echo selected udp port is $udpPort
# subnet=$(docker network inspect bridge --format='{{(index .IPAM.Config 0).Subnet}}')
# echo dockers bridge subnet is $subnet
# broadcast=$(python3 broadcast/src/subnet_to_broadcast.py $subnet)
# echo dockers broadcast address is $broadcast
docker build --rm --tag broadcast ./broadcast
imageId=$(docker image ls --filter "reference=broadcast:*latest*" --format "{{.ID}}")
echo imageId is $imageId
docker run --net custom-net --ip $ip $imageId $broadcast_address $udpPort
containerId=$(docker container ls -a --filter "ancestor=$imageId" --format "{{.ID}}")
echo container id is $containerId
docker cp  $containerId:app/resources/test_environment.postman_environment.json ./
docker cp  $containerId:app/output.log ./
docker stop $containerId

echo environment file successfully extracted