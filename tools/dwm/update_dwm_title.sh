#!/bin/bash

# this will instantly run the first cycle as one cycle is run at the end
# of update_cycle.sh
source ~/bin/update_cycle.sh

#trayer 	--edge top --align right \
#				--widthtype request \
#				--SetDockType true \
#				--transparent true --alpha 255 &
while true
do
    sleep 15
    update_cycle
done
