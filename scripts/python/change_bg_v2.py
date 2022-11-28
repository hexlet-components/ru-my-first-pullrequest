import os
import time
import random
import sys

dir_with_dirs = sys.argv[1] 
if dir_with_dirs[len(dir_with_dirs) - 1] != '/':
    dir_with_dirs += '/'
wallpaper_dirs = os.listdir(dir_with_dirs)
time_to_change_wall = 1 
os.system("touch /tmp/bg_now_o1")
os.system("touch /tmp/bg_now_o2")
os.system("touch /tmp/bg_now_o3")

while True:
    wallpaper_dir = wallpaper_dirs[random.randint(0, len(wallpaper_dirs) - 1)]
    wallpaper_dir = dir_with_dirs + wallpaper_dir 
    if wallpaper_dir[len(wallpaper_dir) - 2] != '/':
        wallpaper_dir += '/'
    wallpapers = os.listdir(wallpaper_dir)

    bg_now_o1 = random.randint(0, len(wallpapers) - 1)
    bg_now_o2 = random.randint(0, len(wallpapers) - 1)
    bg_now_o3 = random.randint(0, len(wallpapers) - 1)

    os.system("echo " + wallpaper_dir + "'" + wallpapers[bg_now_o2] + "'" + ' > /tmp/bg_now_o2')
    os.system("echo " + wallpaper_dir + "'" + wallpapers[bg_now_o1] + "'" + ' > /tmp/bg_now_o1')
    os.system("echo " + wallpaper_dir + "'" + wallpapers[bg_now_o3] + "'" + ' > /tmp/bg_now_o3')
    os.system("swaybg -o DP-1 -i " + wallpaper_dir + "'" + wallpapers[bg_now_o2] + "' " + " -m fill &")
    os.system("swaybg -o eDP-1 -i " + wallpaper_dir + "'" + wallpapers[bg_now_o1] + "' " + " -m fill &")
    os.system("swaybg -o HDMI-A-1 -i " + wallpaper_dir + "'" + wallpapers[bg_now_o3] + "' " + " -m fill &")
    time.sleep(time_to_change_wall * 60)
    os.system("killall swaybg")

