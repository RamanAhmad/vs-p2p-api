FROM ubuntu:24.04
ARG PORT
ARG IP
ARG BROADCAST_ADDR
ARG TEST_SUB
ARG ENVIRONMENT_FILE
RUN echo "Run ${TEST_SUB}-test on ${IP}:${PORT} with broadcast ${BROADCAST_ADDR}"
RUN apt update && apt upgrade -y
RUN apt install curl -y
RUN apt-get install npm -y
WORKDIR /app
RUN npm install -g newman
RUN npm install -g newman-reporter-htmlextra
RUN npm install -S newman-reporter-htmlextra
COPY p2p-postman-collection ./p2p-postman-collection
# COPY out ./out
COPY testcases ./testcases
COPY test_script/run.sh run.sh
COPY broadcast ./broadcast
RUN ls -l /app
RUN chmod +x /app/run.sh
RUN sed -i 's/\r$//' run.sh
ENV envPORT=${PORT}
ENV envBROADCAST_ADDR=${BROADCAST_ADDR}
ENV envTEST_SUB=${TEST_SUB}
ENV envENVIRONMENT_FILE=${ENVIRONMENT_FILE}
# CMD [ "./run_test.sh",${envPORT},${envBROADCAST_ADDR},${envTEST_SUB} ]
CMD [ "sh" ,"-c", "./run.sh $envPORT $envBROADCAST_ADDR $envTEST_SUB $envENVIRONMENT_FILE"]
# CMD ./run_test.sh $PORT $BROADCAST_ADDR $TEST_SUB
