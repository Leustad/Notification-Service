import logging

import requests


def get_release_data(url):
    try:
        r = requests.get(url).json()
        return r['files']['release_data.json']['content']
    except Exception as e:
        logging.error(f'Error when getting GIST data: {e}')


