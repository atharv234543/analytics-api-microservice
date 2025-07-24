#!/bin/bash

source /opt/venv/bin/activate

cd /code
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-127.0.0.1}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app