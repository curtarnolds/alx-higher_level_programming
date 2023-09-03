#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    email = argv[2]
    url = argv[1]
    data = {
        'email': email
    }

    res = requests.post(url, data=data)
    print(res.text)
