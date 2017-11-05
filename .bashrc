#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

(wal -r &)

rel_git_path() {
    if git rev-parse >& /dev/null; then
        realpath --relative-to=$(git rev-parse --git-dir)/../.. "$(pwd)"
    else
        pwd
    fi
}

git_branch() {
    if git rev-parse >& /dev/null; then
        echo "($(git rev-parse --abbrev-ref HEAD))"
    fi
}

allman() {
    USAGE="Usage: allman TOPIC"

    if [[ ! $1 ]]; then
        echo USAGE
        exit 1
    fi

    man $1

    for i in $(seq 1 1 8); do
        man $i $1
    done
}

source ~/.cache/wal/colors.sh

wallaunch() {
    $HOME/.config/wal/wallaunch.sh $@
    source ~/.cache/wal/colors.sh
}

alias walcopy='cp $wallpaper $HOME/Pictures/wallpapers'
alias reset='reset -Q'
alias pacman='pacman --color=auto'
alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ll -a'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'
alias grubcfg='sudo grub-mkconfig -o /boot/grub/grub.cfg'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[0m\]: $(tty): \[\e[1;34m\]$(rel_git_path)\[\e[0m\] $(git_branch)\n\$ '
