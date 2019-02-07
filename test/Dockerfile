FROM ubuntu:bionic-20181204

LABEL maintainer="sameer@damagehead.com"

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \
 && rm -rf /var/lib/apt/lists/*

COPY my.cnf /etc/mysql/my.cnf
# RUN rm /etc/mysql/mysql.conf.d/mysqld.cnf \
#  && mkdir -p /var/run/mysqld/ \
# && chown mysql:mysql /var/run/mysqld \
# && rm -rf /var/lib/mysql \
# && /usr/bin/mysqld_safe --initialize
# && mysql_install_db --user=mysql --datadir=/var/lib/mysql
RUN mkdir -p /var/run/mysqld/ && chown mysql:mysql /var/run/mysqld

VOLUME /var/lib/mysql

CMD ["/usr/bin/mysqld_safe"]
