FROM python:latest

LABEL Maintainer="dev"
WORKDIR /app
COPY src/broadcast_to_postman_environment.py ./
COPY resources resources/
ENTRYPOINT ["python","./broadcast_to_postman_environment.py"]