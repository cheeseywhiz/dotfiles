#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ $(tty) = /dev/tty1 ]]; then
    startx |& sudo tee /dev/tty7 /var/xlog > /dev/null
fi
