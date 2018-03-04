# coding=utf-8
import os
import numpy as np
baseDir = "E:\\pingan\\50种情绪\\video"
audioDir = "E:\mmmm"
os.chdir(audioDir)
file = open('E:\\1.txt')
lines = file.readlines()
aa = []
print lines
for line in lines:
    cmd = "md "+line
    os.system(cmd)
    aa.append(line)
print aa
