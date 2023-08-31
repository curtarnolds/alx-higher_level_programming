#!/bin/bash
# Send a request to a URL, and display the size of the body of the response
curl -s -w "%{size_download}" "$1"
