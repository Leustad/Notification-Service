import datetime
from datetime import datetime as dt


def find_releases(data: dict, date: datetime, list_all:bool, today: bool):
    filtered_data = {}
    for k, v in data.items():
        if date:
            filter_date = dt.strptime(date, "%Y-%m-%d").date()
            if filter_date == dt.strptime(v, "%Y-%m-%d").date():
                filtered_data.update({k: v})
        elif list_all:
            filtered_data = data
        elif today and dt.strptime(v, "%Y-%m-%d").date() == datetime.date.today():
            filtered_data.update({k: v})

    return filtered_data
