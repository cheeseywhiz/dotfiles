#!/bin/bash
# launch.sh <path>

WAL_CACHE=$HOME/.cache/wal
WAL_LAST=$WAL_CACHE/wal

# give wal filename that transcends its tmp directory (for caching)
cd $(dirname $1)
wal -i ./$(basename $1) -a 93

WAL_IMG=$(realpath $(cat $WAL_LAST))
echo $WAL_IMG > $WAL_LAST

cd $WAL_CACHE/wal_chrome
convert $WAL_IMG -scale "1366x768^" -blur "0x10" ./img/theme_ntp_background.jpg
$HOME/.config/wal/chrome_theme.py
