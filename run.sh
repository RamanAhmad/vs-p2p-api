#!/bin/sh
port=$1
./broadcast/run.sh $port
environment="test_environment.postman_environment.json"
mv $environment testcases/$environment
echo $environment
python3 testcases/TestGenerator.py $environment
docker build --rm --tag p2p_collection ./
imageId=$(docker image ls --filter "reference=p2p_collection:*latest*" --format "{{.ID}}")
echo imageId is $imageId
docker run $imageId
containerId=$(docker container ls -a --filter "ancestor=$imageId" --format "{{.ID}}")
echo container id is $containerId
docker cp  $containerId:app/output.log ./