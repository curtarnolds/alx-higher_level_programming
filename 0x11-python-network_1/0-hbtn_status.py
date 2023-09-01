#!/usr/bin/python3
"""A script to fetch `https://alx-intranet.hbtn.io/status`
and uses urllib
"""


if __name__ == "__main__":
    import urllib.request
    
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as\
            response:
        read = response.read()
        print('Body response:')
        print('\t- type: ', type(read))
        print('\t- content: ', read)
        print('\t- utf8 content: ', read.decode('utf-8'))
