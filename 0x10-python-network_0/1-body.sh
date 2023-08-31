#!/bin/bash
# Send a GET request to an URL and display the body of the response only if the response code is 200
curl -sL "$1"
