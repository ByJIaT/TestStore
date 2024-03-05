FROM python:3.11-slim

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/