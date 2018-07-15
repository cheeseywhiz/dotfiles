#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

# (cat ~/.cache/wal/sequences &)

rel_git_path() {
    if git rev-parse >& /dev/null; then
        realpath --relative-to="$(git rev-parse --git-dir)/../.." "$(pwd)"
    else
        pwd
    fi
}

git_branch() {
    if git rev-parse >& /dev/null; then
        echo "($(git rev-parse --abbrev-ref HEAD 2>/dev/null))"
    fi
}

git-diff-all() {
    for file in $(git ls-files -m); do
        git diff $file
    done
}

set-title() {
    ESC="\e"
    OSC="\x5d"
    ST="\x5c"
    TITLE="${USER}: $(date "+%X"): $(rel_git_path) $(git_branch)"
    echo -ne "${ESC}${OSC}0;${TITLE}${ESC}${ST}"
}

# Clean the mirrors
windex() {
    # Fetch | uncomment | write as root to file
    curl "https://www.archlinux.org/mirrorlist/?country=CA&country=FR&country=DE&country=MX&country=GB&country=US&protocol=https&ip_version=4&ip_version=6&use_mirror_status=on" \
        | sed -e 's/#Server/Server/g' \
        | sudo tee /etc/pacman.d/mirrorlist
}

source ~/.cache/wal/colors.sh

alias allman='man -a'
alias s='source ~/.bashrc'
alias walcopy='s && cp $wallpaper $HOME/Pictures/wallpapers'
alias reset='tput reset'
alias pacman='pacman --color=auto'
alias ls='ls -h --color=auto'
alias ll='ls -l'
alias la='ll -a'
alias cdtmp='cd $(mktemp -d)'
alias pipes='pipes.sh -p 20 -r 3000 -t 0 -R'
alias ffind='find / 2>/dev/null | fgrep'
alias grubcfg='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias wallaunch='~/.config/i3/sys_cmd.sh wallaunch'

PS1='$(printf '%.*s' $? $?)\[\e[01;32m\]\u\[\e[0m\]: $(date "+%X"): \[\e[1;34m\]$(rel_git_path)\[\e[0m\] $(git_branch)\n\$ $(set-title)'
export EDITOR=vim
export XDG_CONFIG_HOME=$HOME/.config
export PATH="${PATH}:$HOME/.local/bin"
source /usr/share/nvm/init-nvm.sh

export WS1="chromium --new-window --load-extension=/home/cheese/.cache/wal/wal_chrome"
export WS2=subl
export WS3=st
export WS10="${WS1} --incognito https://www.reddit.com/"
