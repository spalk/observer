# -*- coding: utf-8 -*-

import requests

url = 'http://localhost:8888/observer'
data = {'number': 12524, 'message': 'issue', 'action': 'show'}

r = requests.post(url, data)

print(r.status_code, r.reason)
print(r.text)
