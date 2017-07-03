#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# start x only on Arch terminal #1
if [[ $(tty) = /dev/tty1 ]]; then
    startx

# etc
elif [[ $(tty) = /dev/tty2 ]]; then
    htop
fi
