#
# ~/.bashrc
#

set -x
# If not running interactively, don't do anything
#[[ $- != *i* ]] && return

# parse subdirs
if [ -d "${HOME}/.config/bashrc.d" ]; then
    for x in "${HOME}"/.config/bashrc.d/* ; do
        test -f "$x" || continue  # ignore nonfiles
        test -x "$x" || continue  # ignore nonexecuteable
        . "$x"
    done
fi
