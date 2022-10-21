FROM python:3.10.1-slim-buster

# set working directory

WORKDIR C:\Users\Taylor\Projects\fastapi_advanced_pooling_connection\venv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    &&apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
