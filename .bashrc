#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

(wal -r &)

rel_git_path() {
    if git rev-parse >& /dev/null; then
        echo -n "git: "
        realpath --relative-to=$(dirname $(dirname $(realpath $(git rev-parse --git-dir)))) $(pwd)
    else
        pwd
    fi
}

git_branch() {
    if git rev-parse >& /dev/null; then
        echo "($(git rev-parse --abbrev-ref HEAD))"
    fi
}

alias sudo='sudo'
alias wallaunch='$HOME/.config/wal/launch.py'
alias walnow='cat $HOME/.cache/wal/wal'
alias walcopy='cp $(walnow) $HOME/Pictures/wallpapers'
alias reset='reset -Q'
alias pacman='pacman --color=auto'
alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ls -al'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[0m\]: $(tty): \[\e[1;34m\]$(rel_git_path)\[\e[0m\] $(git_branch)\n\$ '
