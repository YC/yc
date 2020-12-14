#!/bin/sh
curl -X GET "$TIME_API_URL" \
    -H 'Authorization: Basic $TIME_API_KEY' \
    | jq -r '.languages[] | [.key, .total] | @csv' \
    | sed 's/"//g' \
    | python3 process.py
