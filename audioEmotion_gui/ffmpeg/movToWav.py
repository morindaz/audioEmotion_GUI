# coding=utf-8
'''
利用ffmpeg将mov转换成wav格式
1.sox 2.wav -t null /dev/null trim 0 0.5 noiseprof myprofile
2.sox 2.wav 2-noisefree.wav noisered myprofile 0.26
3.ffmpeg -i 2-noisefree.wav -i 2.wmv -sameq vid.wmv
'''
# ffmpeg.exe -i __34.15to38.4_Admiration.mov __34.15to38.4_Admiration.wav
import os
ffmpegDir = "E:\pingan\\Zip\\ffmpeg-20170821-d826951-win64-static\\ffmpeg-20170821-d826951-win64-static\\bin"
#输入视频的目录，需要加上相应的文件夹名称
inDir = "E:\pingan\\fiftyEmotions\\video\\video"
#输出音频的目录，需要加上相应的文件夹名称
outDir = "E:\\audio"
txt = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe', 'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness', 'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy', 'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy', 'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse', 'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust', 'Uneasiness', 'vitality']
#转换到对应的每个视频目录
eachDir = txt[1]
inMovovDir = inDir +"\\"+eachDir
# print formatInDir
outMovDir = outDir+"\\"+eachDir
os.chdir(inMovovDir)

file = open(eachDir+'.txt')
lines = file.readlines()
formatLines = []
for line in lines:
    line = line.strip('\n')
    formatLines.append(line)
print formatLines
# ffmpeg.exe -i __34.15to38.4_Admiration.mov __34.15to38.4_Admiration.wav
basecmd ="ffmpeg.exe -i "
#line为每个mov的名称
os.chdir(ffmpegDir)
for line in formatLines:
    #提取每个mov的名字，将名字和mov分开
    _, audioname = os.path.split(line)
    filestr, postfix = os.path.splitext(audioname)
    itemCMD = basecmd+inMovovDir+"\\"+line+" "+outMovDir+"\\"+filestr+".wav"
    os.system(itemCMD)
    print itemCMD
