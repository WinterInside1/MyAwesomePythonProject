FROM python:3.8-alpine


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /

RUN pip3 install --upgrade pip; \
pip3 install -r /requirements.txt

COPY ./entrypoint.sh .

COPY . /app


WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]