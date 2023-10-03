import argparse
import os
import sys

import requests

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from clients.ntfy import notify

host_domain = 'http://127.0.0.1:33510'

parser = argparse.ArgumentParser(
    prog='Notify',
    description='Sends a notification about the release dates',
    epilog='Happy Notifying'
)

parser.add_argument('-d', '--date', help='Date you want to check')
parser.add_argument('-l', '--list_all', type=bool, help='Lists All Releases')
parser.add_argument('-t', '--today', type=bool, help='Checks for today\'s releases')

args = parser.parse_args()

# TODO: Change this HTTP Req to find_releases() func call
r = requests.get(
    url=f'{host_domain}/remind?date={args.date}'
)

if r.json():
    notify(r.json())
    print(r.json())
