#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response
"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    query_args = {}
    query_args['email'] = argv[2]
    data = parse.urlencode(query_args).encode('utf-8')
    url_args = request.Request(argv[1], data)
    with request.urlopen(url_args) as response:
        print(response.read().decode('utf-8'))
