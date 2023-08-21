FROM python:3.8-slim

LABEL MAINTAINER="zhisen"

COPY . /app    

WORKDIR /app 

RUN pip3 install -r requirements.txt

RUN python3 -m pytest

ENTRYPOINT python3 app.py





