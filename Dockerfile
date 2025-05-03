FROM python:3.11-alpine

COPY . /base-api

WORKDIR /base-api

RUN pip3 install -r requirements.txt
