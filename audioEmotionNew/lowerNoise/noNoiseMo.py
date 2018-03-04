# coding=utf-8
'''
This is a file to remove noise background by using sox software.
1.sox 2.wav -t null /dev/null trim 0 0.5 noiseprof myprofile
2.sox 2.wav 2-noisefree.wav noisered myprofile 0.26
'''
import os
import time
import glob
import pandas as pd
import numpy as np

#输入视频的目录，需要加上相应的文件夹名称
inDir = "C:\\Users\\Mypc\\Desktop\\morindaz\\audio"
#输出音频的目录，需要加上相应的文件夹名称
outDir = "C:\\Users\\Mypc\\Desktop\\morindaz\\out"
cmdPath ="C:\\Program Files (x86)\\sox-14-4-2"
txt = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe', 'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness', 'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy', 'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy', 'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse', 'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust', 'Uneasiness', 'vitality']
#转换到对应的每个视频目录
for eachDir in txt:
    inMovovDir = inDir +"\\"+eachDir
# print formatInDir
    outMovDir = outDir+"\\"+eachDir
    os.chdir(inMovovDir)
    csvx_list = glob.glob('*.wav') #列出每个文件夹下面的wav文件
    print('总共发现%s个wav文件' % len(csvx_list))
    os.chdir(cmdPath) #转到sox对应的目录
    for line in csvx_list: #每个文件夹下面的csvx_list中的文件取出来
        #提取每个mov的名字，将名字和mov分开
        _, audioname = os.path.split(line)
        filestr, postfix = os.path.splitext(audioname)
        cmd1 = "sox %s -t null /dev/null trim 0 0.5 noiseprof %s"% (inMovovDir+"\\"+line,outMovDir+"\\"+filestr)
        cmd2 = "sox %s %s noisered %s 0.26"% (inMovovDir+"\\"+line,outMovDir+"\\"+filestr+"Noise.wav",outMovDir+"\\"+filestr)
        print cmd1
        print cmd2
        os.system(cmd1)
        os.system(cmd2)
