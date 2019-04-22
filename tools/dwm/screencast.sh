#!/bin/bash

# not so simple one-liner for capturing video and audio for a screencast
# the state of this is "works for me"

TIMESTAMP=`date +%Y-%m-%d_%H-%M-%S`
FILENAME="cast.${TIMESTAMP}.mkv"
TARGETDIR="${HOME}/videos/"

#screen
FPS=30
RES="1920x1080"
XDISPLAY=":0.0"

#sound
MONITOR="alsa_output.pci-0000_00_1f.3.analog-stereo.monitor"
MIC="alsa_input.pci-0000_00_1f.3.analog-stereo"

#coder
CRF=0  # 0=lossless 50=maximum loss, below ~20 perceptionally lossless
PRESET="ultrafast"  # let's do not waste time here to save some bytes

set -x
ffmpeg \
	-thread_queue_size 64 \
	-video_size ${RES}\
	-framerate ${FPS} \
	-f x11grab -r ${FPS} -i ${XDISPLAY} \
	-f pulse -i ${MIC} \
	-f pulse -i ${MONITOR} \
	-filter_complex amerge \
	-c:v libx264 -crf ${CRF} -preset ${PRESET} \
	-y "${TARGETDIR}${FILENAME}"
