FROM python:3.11.9-slim-bookworn

WORKDIR /app

COPY requirements.txt ./

COPY . .


RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    wget unzip && \
    rm -rf /var/lib/apt/lists/*
