!/bin/bash

cd ~
export SWAYSOCK=/run/user/$(id -u)/sway-ipc.$(id -u).$(pgrep -x sway).sock
export _JAVA_AWT_WM_NONREPARENTING=1
export XCURSOR_SIZE=24
