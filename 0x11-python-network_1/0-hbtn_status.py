#!/usr/bin/python3
"""A script to fetch `https://alx-intranet.hbtn.io/status`"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        read = response.read()
        print('Body response:')
        print('\t- type: ', type(read))
        print('\t- content: ', read)
        print('\t- utf8 content: ', read.decode('utf-8'))
