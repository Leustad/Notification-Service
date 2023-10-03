import logging

import requests

topic = 'reminder'


def notify(msg):
    try:
        if msg:
            temp = ''
            for k, v in msg.items():
                temp += f'{k}: {v}'

            r = requests.post(
                url=f'https://ntfy.snowy.land/{topic}',
                data=f'{temp}'.encode('utf-8'),
                headers={
                    'Title': 'Game Release(s) Found !!',
                    'Priority': 'urgent',
                    'tags': 'partying_face'
                }
            )
    except Exception as e:
        logging.error(f'Error while notifying: {e}')
