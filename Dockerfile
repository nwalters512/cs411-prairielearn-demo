FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev sudo \
  && DEBIAN_FRONTEND=noninteractive apt-get -yq install mysql-server \
  && rm -rf /var/lib/apt/lists/* \
  && python3 -m pip install --upgrade pip \
  && python3 -m pip install sqlparse mysql-connector-python

COPY my.cnf /etc/mysql/my.cnf

RUN mkdir -p /var/run/mysqld/ && chown mysql:mysql /var/run/mysqld

VOLUME /var/lib/mysql
