import logging

import requests

topic = 'reminder'


def notify(msg):
    try:
        r = requests.post(
            url=f'https://ntfy.snowy.land/{topic}',
            data=f'{msg} 😀'.encode('utf-8')
        )
    except Exception as e:
        logging.error(f'Error while notifying: {e}')
