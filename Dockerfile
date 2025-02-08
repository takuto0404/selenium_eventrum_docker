FROM python:3.11.9-slim-bookworn

WORKDIR /app

COPY requirements.txt ./

COPY . .
