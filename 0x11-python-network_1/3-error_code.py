#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url_args = request.Request(argv[1])
    try:
        with request.urlopen(url_args) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
