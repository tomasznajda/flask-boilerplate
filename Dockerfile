FROM python:2.7

MAINTAINER Tomasz Najda "hello@tomasznajda.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip &&\
    pip install --upgrade enum34

COPY . /app

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 7100