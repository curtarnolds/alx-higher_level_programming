#!/usr/bin/python3
"""Sends a POST request to a URL with a given letter to
http://0.0.0.0:5000/search_user and displays the body of the response
"""
if __name__ == '__main__':
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    try:
        data = {'q': argv[1]}
    except IndexError:
        data = {'q': ''}
    res = requests.post(url, data=data)

    try:
        json_str = res.json()
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

    if len(json_str) == 0:
        print('No result')
    else:
        print(f"[{json_str.id} {json_str.name}]")
