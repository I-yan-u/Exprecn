#!/usr/bin/bash
# Start server (dev or prod)
dev="-d"
prod="-p"

if [[ "$1" == "$dev" ]]; then
    echo 'Starting Development server'
    tmux new-session -d python3 -m web_dynamic.index
    tmux new-session -d python3 -m api.v1.app
elif [[ "$1" == "$prod" ]]; then
    echo 'Startig Production server'
else
    echo 'Invalid option. Use -d for development or -p for production.'
fi

