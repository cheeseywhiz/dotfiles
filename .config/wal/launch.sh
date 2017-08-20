#!/bin/bash
# launch.sh <path>

cd $HOME/.cache/wal

wal -i $1 -a 93
rm ./wal_chrome/"Cached Theme.pak" |& sudo tee /dev/null > /dev/null
convert -scale "1366x768^" -blur "0x10" $(cat ./wal) ./wal_chrome/img/theme_ntp_background.jpg
$HOME/.config/wal/chrome_theme.py
