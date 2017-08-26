#!/bin/bash
USAGE="Usage: launch.sh <path>"

if [[ ! $1 ]]; then
    echo $USAGE
    exit 1;
fi

WAL_CACHE=$HOME/.cache/wal

# give wal ./filename only for consistent caching
cd $(dirname $1)
wal -i ./$(basename $1) -a 93
WAL_IMG=$(realpath $(cat $WAL_CACHE/wal))
echo $WAL_IMG > $WAL_CACHE/wal

convert $WAL_IMG -scale "1366x768^" -blur "0x10" $WAL_CACHE/wal_chrome/img/theme_ntp_background.jpg
$HOME/.config/wal/chrome_theme.py
