#!/bin/bash

source ~/.bashrc

always_init() {
    ~/.config/devilspie2/launch.sh &
    compton -bc --config ~/.config/compton.conf &
    polybar_launch &
}

once_init() {
    synclient HorizEdgeScroll=1 VertEdgeScroll=1 VertScrollDelta=-111 LBCornerButton=1 RBCornerButton=2 &
    wal_reddit &
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
