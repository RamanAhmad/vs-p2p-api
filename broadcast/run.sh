#!/bin/sh
# Author : Ansgar Deuschel
udpPort="$1"
echo selected udp port is $udpPort
subnet=$(docker network inspect bridge --format='{{(index .IPAM.Config 0).Subnet}}')
echo dockers bridge subnet is $subnet
broadcast=$(python3 src/subnet_to_broadcast.py $subnet)
echo dockers broadcast address is $broadcast
docker build --rm --tag broadcast ./
imageId=$(docker image ls --filter "reference=broadcast:*latest*" --format "{{.ID}}")
echo imageId is $imageId
docker run $imageId $broadcast $udpPort
containerId=$(docker container ls -a --filter "ancestor=$imageId" --format "{{.ID}}")
echo container id is $containerId
docker cp  $containerId:app/resources/test_environment.postman_environment.json ./
echo environment file successfully extracted