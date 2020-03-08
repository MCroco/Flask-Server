FROM debian:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install apache2 -y && \
    apt-get install libapache2-mod-wsgi-py3 python-dev -y

RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf

WORKDIR /app
EXPOSE 80

COPY apache-foreground /usr/local/bin
RUN chmod +x /usr/local/bin/apache-foreground
CMD apache-foreground