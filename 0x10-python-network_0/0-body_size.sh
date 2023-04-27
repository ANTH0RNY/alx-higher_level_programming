#!/bin/bash
#Size of HTTP responce
curl -s "$1" | wc -c
