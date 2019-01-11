#!/usr/bin/env python

import requests

#print(requests.__version__)

#r = requests.get('http://google.com')
#print(r.text)
#print(r.status_code)

r = requests.get('https://github.com/Blazusiak/CMPUT404/raw/master/script.py')

print(r.text)