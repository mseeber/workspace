#!/bin/bash

wp_dir="$HOME/.wallpaper/"

lst_wp() {
	echo -ne $(find ${wp_dir} -type f -print0 | xargs -0 -n1 echo)
}

rnd_wp() {
	echo -ne $(shuf -n1 -e $(lst_wp))
}

feh --bg-scale $(rnd_wp)
