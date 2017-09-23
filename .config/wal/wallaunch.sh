#!/bin/bash
USAGE="Usage: wallaunch.sh PATH"

if [[ ! $1 ]]; then
    echo $USAGE
    exit 1;
fi

wal -i $1 -a 93
$HOME/.config/wal/chrome_theme.py
