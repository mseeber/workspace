#!/bin/bash

# screenshot tool
# 
# usage: screenshot [delay]
# creates a screenshot in png format in $HOME/Pictures
# first parameter is an optional delay in seconds

screenshot() {
	local delay="${1:-0}"  # default to "no delay" TODO can be better?
	local timestamp=`date +%Y-%m-%d_%H:%M:%S`
	
	sleep "${delay}"
	import -window root "$HOME/Pictures/screenshot-${timestamp}.png"
}

screenshot "${1}"
