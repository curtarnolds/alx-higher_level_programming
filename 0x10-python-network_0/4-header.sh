#!/bin/bash
# Sends a GET request to the URL with header variable "X-School-User-Id" set to 98, and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
