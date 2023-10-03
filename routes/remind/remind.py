from ast import literal_eval

from fastapi import APIRouter, Depends

from routes.pydantic_models.models import Remind
from routes.remind.remind_services import find_releases, make_filter
from routes.utils import get_release_data
from clients.infisical import GIST_URL
from clients.ntfy import notify

remind_router = APIRouter(prefix='/remind', tags=['Reminder'])


@remind_router.get('')
def remind(params: Remind = Depends(), send_notification: bool = False):
    data = literal_eval(get_release_data(url=GIST_URL))
    filters = make_filter(params)
    filtered_data = find_releases(
        data=data,
        filters=filters
    )

    if send_notification:
        notify(filtered_data)
    return filtered_data
