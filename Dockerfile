FROM python:3.7-alpine
MAINTAINER Tien Do

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
RUN chown user:user -R /app/
USER user