#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

(wal -r &)

rel_git_path() {
    if git rev-parse >& /dev/null; then
        realpath --relative-to="$(git rev-parse --git-dir)/../.." "$(pwd)"
    else
        pwd
    fi
}

git_branch() {
    if git rev-parse >& /dev/null; then
        echo "($(git rev-parse --abbrev-ref HEAD))"
    fi
}

source ~/.cache/wal/colors.sh

wallaunch() {
    $HOME/.config/wal/wallaunch.sh $@
    source ~/.cache/wal/colors.sh
}

alias allman='man -a'
alias walcopy='cp $wallpaper $HOME/Pictures/wallpapers'
alias reset='reset -Q'
alias pacman='pacman --color=auto'
alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ll -a'
alias s='source ~/.bashrc'
alias cdtmp='cd $(mktemp -d)'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'
alias ffind='find / 2>/dev/null | fgrep'
alias grubcfg='sudo grub-mkconfig -o /boot/grub/grub.cfg'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[0m\]: $(tty): \[\e[1;34m\]$(rel_git_path)\[\e[0m\] $(git_branch)\n\$ '
