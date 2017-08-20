#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

(wal -r &)

alias wallaunch='$HOME/.config/wal/launch.sh'
alias reset='reset -Q'
alias pacman='pacman --color=auto'
alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ls -al'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[0m\]: $(tty): \[\e[1;34m\]\w\[\e[0m\]\n\$ '
