#!/bin/bash
# Send a DELETE request to the URL passed as first argument and displays the body of the response
curl -sX DELETE "$1"
