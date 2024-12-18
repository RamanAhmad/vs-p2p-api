#!/bin/sh
#ARG 1: port
#ARG 2: target ("sol" or "com")
port=$1
target=$2
ip=172.99.0.100
broadcast_addr=172.99.255.255
docker_net=custom-net
docker build --rm --tag p2p_collection_sol \
 --build-arg PORT=$port \
 --build-arg IP=$ip \
 --build-arg BROADCAST_ADDR=$broadcast_addr \
 --build-arg TEST_SUB=$target \
 --build-arg ENVIRONMENT_FILE="broadcast/resources/test_environment.postman_environment.json" \
 --progress=plain ./
imageId=$(docker image ls --filter "reference=p2p_collection_sol:*latest*" --format "{{.ID}}")
echo imageId is $imageId
docker run --net $docker_net --ip $ip $imageId
containerId=$(docker container ls -a --filter "ancestor=$imageId" --format "{{.ID}}")
echo container id is $containerId
mkdir test_results
mkdir test_results/$target

docker cp  $containerId:app/output.log ./test_results/$target/
docker cp  $containerId:app/out/test_cases/test_cases.csv ./test_results/$target/
docker cp  $containerId:app/broadcast/resources/test_environment.postman_environment.json ./test_results/$target/
docker cp  $containerId:app/broadcast/resources/test_environment.postman_environment.json ./test_results/$target/
docker cp  $containerId:app/newman ./test_results/$target/

docker stop $containerId
docker container rm $containerId