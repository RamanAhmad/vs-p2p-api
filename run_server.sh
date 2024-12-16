# docker network rm custom-net
docker network create --subnet=172.19.0.0/16 custom-net
serverImageId=$1
docker run --net custom-net --ip 172.19.0.2 $serverImageId