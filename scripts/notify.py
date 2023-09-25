import argparse

import requests

host_domain = 'http://127.0.0.1:8001'

parser = argparse.ArgumentParser(
    prog='Notify',
    description='Sends a notification about the release dates',
    epilog='Happy Notifying'
)

parser.add_argument('-d', '--date', help='Date you want to check')
parser.add_argument('-l', '--list_all', type=bool, help='Lists All Releases')
parser.add_argument('-t', '--today', type=bool, help='Checks for today\'s releases')

args = parser.parse_args()

requests.get(
    url=f'{host_domain}/remind?date={args.date}'
)
