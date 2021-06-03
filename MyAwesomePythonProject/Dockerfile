FROM python:3.8.3-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /

RUN pip3 install --upgrade pip; \
pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app