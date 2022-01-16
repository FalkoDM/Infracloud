FROM ubuntu:18.04

RUN apt-get update -y 
RUN apt-get install -y apache2
RUN a2enmod rewrite
RUN sed -i 's/^Listen 80/Listen 8081/' /etc/apache2/ports.conf
RUN sed -i 's/^<VirtualHost \*:80>/<VirtualHost *:8081>/' /etc/apache2/sites-available/000-default.conf
EXPOSE 8081
CMD apachectl -D FOREGROUND