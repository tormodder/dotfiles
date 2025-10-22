#!/bin/sh
discord &
firefox &
picom --backend xrender --vsync --config ~/.config/picom/picom.conf &
flameshot &
dunst &
obsidian &
export LIBGL_KOPPER_DISABLE=1 
