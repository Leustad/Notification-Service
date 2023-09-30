from ast import literal_eval

from fastapi import APIRouter

from routes.remind_services import find_releases
from routes.utils import get_release_data
from services.infisical import GIST_URL
from services.ntfy import notify

remind_router = APIRouter(prefix='/remind', tags=['Reminder'])


@remind_router.get('')
def remind(today: bool = True, list_all: bool = False, date: str = None):
    data = literal_eval(get_release_data(url=GIST_URL))
    filtered_data = find_releases(data=data, date=date, list_all=list_all, today=today)

    notify(filtered_data)
    return filtered_data
