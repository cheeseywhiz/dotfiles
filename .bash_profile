#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && source ~/.bashrc

sudo chmod 666 /sys/class/backlight/intel_backlight/brightness

if [[ $(tty) = /dev/tty1 ]]; then
    startx |& sudo tee /dev/tty7 /var/xlog > /dev/null &
fi
