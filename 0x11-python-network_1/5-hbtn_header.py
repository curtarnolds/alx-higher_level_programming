#!/usr/bin/python3
"""Send a request to a URL and display the header variable X-Request-Id"""
import requests
from sys import argv


res = requests.get(argv[1])
print(res.headers.get('X-Request-Id'))
