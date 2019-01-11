#!/usr/bin/env python

import requests

#print(requests.__version__)

#r = requests.get('http://google.com')
#print(r.text)
#print(r.status_code)

r = requests.get('https://raw.githubusercontent.com/Blazusiak/CMPUT404LAB1/master/script.py')

print(r.text)