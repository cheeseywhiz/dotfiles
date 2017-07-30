#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# start x only on Arch terminal #1
if [[ $(tty) = /dev/tty1 ]]; then
    startx |& sudo tee /dev/tty7 | sudo tee /var/xlog > /dev/null

# etc
elif [[ $(tty) = /dev/tty2 ]]; then
    htop

# shut down the computer when logging in on terminal 6
elif [[ $(tty) = /dev/tty6 ]]; then
    shutdown
fi
