import datetime
from datetime import datetime as dt


def make_filter(params):
    if params.today:
        return {'today': True}
    elif params.list_all:
        return {'list_all': True}

    if any([params.name, params.date]):
        return{
            'name': params.name,
            'date:': params.date
        }


def find_releases(data: dict, filters: dict):
    filtered_data = {}
    if not filters or filters.get('list_all'):
        return data

    for k, v in data.items():
        if filters.get('date'):
            filter_date = dt.strptime(filters['date'], "%Y-%m-%d").date()
            if filter_date == dt.strptime(v, "%Y-%m-%d").date():
                filtered_data.update({k: v})
        if filters.get('name'):
            if filters['name'].lower() in k.lower():
                filtered_data.update({k: v})
        elif filters.get('today') and dt.strptime(v, "%Y-%m-%d").date() == datetime.date.today():
            filtered_data.update({k: v})

    return filtered_data
