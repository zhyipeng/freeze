#!/bin/bash
set -e

../venv/bin/uwsgi --ini ../conf/dada.ini

exec "$@"