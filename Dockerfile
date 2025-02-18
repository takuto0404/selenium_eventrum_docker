FROM python:3.12-slim
USER root

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/* \

RUN python3 -m venv /venv

RUN /venv/bin/pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN /venv/bin/pip install -r /app/requirements.txt

EXPOSE 4444