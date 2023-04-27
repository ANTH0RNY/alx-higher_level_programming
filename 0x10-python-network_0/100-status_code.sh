#!/bin/bash
# Send a GET to URL and display responce status code
curl -s -o /dev/null -w "%{http_code}" "$1"
