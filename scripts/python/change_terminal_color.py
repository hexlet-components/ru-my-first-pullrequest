import sys
import os

os.system("swaymsg -t get_outputs | grep focused > /tmp/outputs_inf")

bg_now_o1 = os.system("cat /tmp/bg_now_o1")
bg_now_o2 = os.system("cat /tmp/bg_now_o2")

print(bg_now_o1, bg_now_o2)
