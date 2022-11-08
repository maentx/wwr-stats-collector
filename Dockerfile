# syntax=docker/dockerfile:1
FROM python:latest
# WORKDIR /code
RUN apt-get update && apt-get dist-upgrade -y && apt-get -y install vim less
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# COPY . .
