#!/bin/bash

source ~/.bashrc

always_init() {
    ~/.config/devilspie2/launch.sh &
    compton -bc --config ~/.config/compton.conf &
    polybar_launch &
}

once_init() {
    synclient HorizEdgeScroll=1 VertEdgeScroll=1 VertScrollDelta=-111 LBCornerButton=1 RBCornerButton=2 &
}

wallaunch () {
    wal -i $1 -a 93
}

walR() {
    # wal -R -a 93
    wallaunch $wallpaper
    ~/.config/wal/chrome_theme.py
}

wal_wallpapers() {
    wallaunch ~/Pictures/wallpapers
}

wal_reddit() {
    wallaunch $(collect -v reddit -n -r -a)
}

polybar_launch() {
    ~/.config/polybar/launch.sh
}

$@
