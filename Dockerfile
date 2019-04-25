# Version 0.0.1
FROM python:3.7.3-stretch as django
MAINTAINER Nick "zhyipeng@outlook.com"
ENV REFRESHED_AT 2019-04-25

COPY deploys/pip/pip.conf /root/.pip/pip.conf

RUN mkdir -p /srv/www/freeze-app/freeze
RUN mkdir -p /srv/www/freeze-app/logs
RUN mkdir -p /srv/www/freeze-app/public_html
ADD deploys/uwsgi/freeze.ini  /srv/www/freeze-app/conf/
ADD deploys/docker-entrypoint.sh /docker-entrypoint.sh

# Copy all our files into the image.
COPY . /srv/www/freeze-app/freeze/

WORKDIR /srv/www/freeze-app/
RUN python -V
RUN pip3 install virtualenv
RUN virtualenv venv

WORKDIR /srv/www/freeze-app/freeze/
RUN ../venv/bin/python -V
RUN ../venv/bin/pip -V
RUN ../venv/bin/pip install -r requirements.txt
RUN ../venv/bin/pip install uwsgi
RUN ../venv/bin/python manage.py collectstatic

ENTRYPOINT ["sh", "/docker-entrypoint.sh"]

FROM nginx:alpine as nginx

# ensure www-data user exists
RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

RUN apk add --no-cache bash
RUN mkdir -p /srv/www/freeze-app/logs
ADD deploys/nginx/freeze.conf /etc/nginx/conf.d/
ADD deploys/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=django /srv/www/freeze-app/public_html /srv/www/freeze-app/public_html