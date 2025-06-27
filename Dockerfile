FROM python:3.10

WORKDIR /App

COPY requirements.txt /App
RUN pip install -r requirements.txt 



