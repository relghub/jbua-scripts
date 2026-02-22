import os
import shutil
fold = 'TheWheelMatching'
ext = '.ogg'
files = os.listdir(path='audio')
for file in files:
    stat = file.replace(ext,'').split('_',1) 
    shutil.copy('audio/' + file,fold + '/' + stat[0] + '/' + stat[1] + ext)
