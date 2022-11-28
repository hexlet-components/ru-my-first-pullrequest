import os
import random

ext = input('file extension: ')
src = input('source direction: ')
output = input('distination direction: ')

if ext[0] == '.': ext = ext[1:]
if src[len(src) - 1] != '/': src = src + '/'
if output[len(output) - 1] != '/': output = output + '/'


files_names = os.listdir(src)

os.system('mkdir ' + output)
for file in files_names:
    temp_str = ''
    for k in range(40):
        if random.randint(0, 1):
            temp_str += chr(random.randint(97, 122))
        else:
            temp_str += chr(random.randint(48, 57))

    temp_str = temp_str + '.' + ext
    print(temp_str)
    os.system('cp ' + src + "'" + file + "' " + output + temp_str)

