FROM python:3.6

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

ADD . /usr/src/app
