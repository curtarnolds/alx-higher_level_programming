#!/bin/bash
# Takes a URL and displays all HTTP methods the server will accept
curl -sI | grep -i "Allow" | cut -d " " -f 2-
