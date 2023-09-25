import json
import datetime
from datetime import datetime as dt
from fastapi import APIRouter

from services.ntfy import notify

remind_router = APIRouter(prefix='/remind', tags=['Reminder'])


@remind_router.get('')
def remind(today: bool = True, list_all: bool = False, date: str = None):
    with open('./files/data.json', 'r') as file:
        temp = {}
        data = json.loads(file.read())
        for k, v in data.items():
            if date:
                filter_date = dt.strptime(date, "%Y-%m-%d").date()
                if filter_date == dt.strptime(v, "%Y-%m-%d").date():
                    temp.update({k: v})
            elif list_all:
                temp = data
            elif today and dt.strptime(v, "%Y-%m-%d").date() == datetime.date.today():
                temp.update({k: v})

    notify(temp)
    return temp
