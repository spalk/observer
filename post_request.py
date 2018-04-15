# -*- coding: utf-8 -*-

import requests
import psutil


# Memory in Mb
memory_total = psutil.virtual_memory().total/1024/1024 
memory_availalbe = psutil.virtual_memory().available/1024/1024

# Disk
disk_total = psutil.disk_usage('/')
#sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)

data = {
    'server':[
        {'param':'value'},
        {'param':'value'},
    ]
    'process':[
        {'name':'status'},
        {'name':'status'},
    ]
}




url = 'http://localhost:8888/observer'
data = {'number': 12524, 'message': 'issue', 'action': 'show'}

r = requests.post(url, data)

print(r.status_code, r.reason)
print(r.text)
