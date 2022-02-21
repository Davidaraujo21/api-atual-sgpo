FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .