#!/bin/bash

# not so simple one-liner for capturing video and audio for a screencast
# the state of this is "works for me"

ffmpeg -thread_queue_size 64 \ # avoid some race conditions at startup
	-loglevel error \ # this avoids unneeded spam on console
	-video_size 1920x1080 \
	-framerate 25 \
	-f x11grab -i :0.0 \
	-f pulse -i alsa_output.pci-0000_00_1b.0.analog-stereo.monitor \
	-af aresample=async=1 \ #avoid bigger audio artifacts and asyncronous AV at cost of samplerate conversion
	-c:v libx264 -crf 0 -preset ultrafast \ #do not waste too much CPU cycles on coding
	/dev/shm/recapture.mkv #TODO more sane location for output file

