FROM python:3.11-slim
USER root

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

RUN du