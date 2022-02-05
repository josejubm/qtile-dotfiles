#!/bin/sh

#wallpaper

feh --bg-fill ~/Imágenes/wallpapers/katana.png &

nm-applet &
picom &

xfce4-power-manager &

#discord &

# systray battery icon
cbatticon -u 5 &

# systray volume
volumeicon &
 
/usr/lib/xfce4/notifyd/xfce4-notifyd &   