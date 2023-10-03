#!/bin/bash

pushd /home/leustad/repos/Notification-Service/
export $(grep -v '^#' .env | xargs)
source //home/leustad/repos/Notification-Service/venv/bin/activate
python /home/leustad/repos/Notification-Service/main.py


uvicorn main:app --host 0.0.0.0 --port 8001 --reload