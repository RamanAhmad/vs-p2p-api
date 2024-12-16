FROM ubuntu:24.04
RUN apt update && apt upgrade -y
RUN apt install curl -y
RUN apt-get install npm -y
WORKDIR /app
RUN npm install -g newman
COPY p2p-postman-collection ./
COPY out/test_cases ./
COPY testcases/test_environment.postman_environment.json ./ 
COPY run_test.sh ./
COPY output.log ./
CMD ["./run_test.sh"]