#!/bin/bash

# set a short time untill screen turns off
xset dpms 10 10 10

# turn it off instantly once
xset dpms force off

# lock the screen
slock

# after unlocking, reset time until screen turns off
xset dpms 600 600 600

