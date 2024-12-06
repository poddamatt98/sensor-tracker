FROM python:3.12-slim-bookworm

WORKDIR /app

COPY ./requirements.in /app/requirements.in

RUN apt update && apt install -y curl

RUN pip install pip-tools
RUN pip-compile /app/requirements.in --output-file /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
