# syntax=docker/dockerfile:1.4
FROM python:3.9-alpine

# Create app dir
WORKDIR /usr/src/api

# Instal dependencies
ADD requirements.txt /usr/src/api/
RUN pip3 install -r requirements.txt

ADD . /usr/src/api

RUN chmod +x scripts/start.sh
ENTRYPOINT ["scripts/start.sh"]