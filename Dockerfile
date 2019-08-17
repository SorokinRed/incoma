FROM python:3.7.4-buster

USER root

RUN mkdir -p /var/www/autotests
RUN mkdir -p /var/www/reports
WORKDIR /var/www/autotests
COPY . .
RUN pip install -r requirements.txt
