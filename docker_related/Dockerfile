FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

CMD python app/script.py
