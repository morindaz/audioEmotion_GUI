# coding=utf-8
# ffmpeg.exe -i __34.15to38.4_Admiration.mov __34.15to38.4_Admiration.wav
'''
批量生成对应文件夹下面的所有文件名称，保存成txt格式。
'''

import os
ffmpegDir = "E:\pingan\压缩包\\ffmpeg-20170821-d826951-win64-static\\ffmpeg-20170821-d826951-win64-static\\bin"
#输入视频的目录，需要加上相应的文件夹名称
inDir = "E:\pingan\\fiftyEmotions\\video\\video"
#输出音频的目录，需要加上相应的文件夹名称
outDir = "E:\\audio"
file = open('E:\\1.txt')
lines = file.readlines()
txt = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe', 'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness', 'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy', 'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy', 'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse', 'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust', 'Uneasiness', 'vitality']

aa = []
for line in txt:
    aa.append(line)
    txtDir = inDir + "\\" + line #到达每个视频文件夹，里面包含100个样本
    os.chdir(txtDir)
    cmd ="dir *.* /b >"+line+".txt"
    os.system(cmd)
