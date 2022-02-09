import requests
from . import secret


def send_line(res):
    line_notify_token = secret.secret
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': [res[i] for i in range(len(res))]}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)