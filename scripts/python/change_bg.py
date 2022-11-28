import os
import time
import random
import sys

wallpaper_dir = sys.argv[1] 
if wallpaper_dir != '/':
    wallpaper_dir += '/'
wallpapers = os.listdir(wallpaper_dir)
time_to_change_wall = 10 
os.system("touch /tmp/bg_now_o1")
os.system("touch /tmp/bg_now_o2")

while True:
    bg_now_o1 = random.randint(0, len(wallpapers) - 1)
    bg_now_o2 = random.randint(0, len(wallpapers) - 1)

    os.system("echo " + wallpaper_dir + "'" + wallpapers[bg_now_o2] + "' > /tmp/bg_now_o2")
    os.system("echo " + wallpaper_dir + "'" + wallpapers[bg_now_o1] + "' > /tmp/bg_now_o1")
    os.system("swaybg -o DP-1 -i " + wallpaper_dir + "'" + wallpapers[bg_now_o2] + "' " + " -m fill &")
    os.system("swaybg -o eDP-1 -i " + wallpaper_dir + "'" + wallpapers[bg_now_o1] + "' " + " -m fill &")
    time.sleep(time_to_change_wall * 60)
    os.system("killall swaybg")
