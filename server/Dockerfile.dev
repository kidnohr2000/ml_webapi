FROM python:3.6.8

ENV APP_PATH '/app'
ENV DEBIAN_FRONTEND noninteractive
ENV TZ JST-9
ENV TERM xterm

WORKDIR $APP_PATH/

COPY ./requirements.txt ./

RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install locales

RUN locale-gen en_US.UTF-8

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .