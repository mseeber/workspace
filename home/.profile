#
# ~/.profile
#

# parse subdirs
if [ -d "${HOME}/.config/profile.d" ]; then
    for x in "${HOME}"/.config/profile.d/* ; do
        test -f "$x" || continue  # ignore nonfiles
        test -x "$x" || continue  # ignore nonexecuteable
        . "$x"
    done
fi
