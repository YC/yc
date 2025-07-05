#!/bin/bash
curl -X GET "$TIME_API_URL" -H "Authorization: Basic $TIME_API_KEY" \
    | jq -r '.languages[] | [.key, .total] | @csv' \
    | sed 's/"//g' \
    | python3 process.py \
    | cat README.md.template - > README.md

# When line is found, if subsequent line is not empty, exit 1
if awk '/^#### Personal Coding Activity/ {found=1; next} found && NF {exit 1}' README.md; then
    sed -i '/^#### Personal Coding Activity (past 7 days)$/d' README.md
    truncate -s -1 README.md
fi
