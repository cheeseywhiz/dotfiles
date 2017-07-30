#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

(wal -r &)

alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ls -al'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[00m\]@\[\e[01;32m\]\h\[\e[00m\]: \[\e[1;34m\]\w\[\e[0m\] $ '
