#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ $(tty) = /dev/tty1 ]]; then
    startx |& sudo tee /dev/tty7 | sudo tee /var/xlog > /dev/null
fi
