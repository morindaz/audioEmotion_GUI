# coding=utf-8
'''
拼接每个文件夹下面的所有csv变成一个整体的。一共有50个
可以将多个csv文件拼接成一个，只有一个header
输出到  E:\pingan\audioEmotion\audioEmotionNew\feature
'''
import os
import time
import glob
import pandas as pd

basicPath = "C:\\Users\\Mypc\\Desktop\\morindaz\\audios\\csvFeature\\"   #54个csv的路径
outPath = "C:\\Users\\Mypc\\Desktop\\morindaz\\audios\\combine50\\"     #拼接完csv的输出路径
txt = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe',
       'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness',
       'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy',
       'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy',
       'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse',
       'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust',
       'Uneasiness', 'vitality']

def combine(item):
    csvx_list = glob.glob('*.csv')
    print('总共发现%s个CSV文件' % len(csvx_list))
    time.sleep(2)
    print('正在处理............')
    df = pd.DataFrame()
    for i in csvx_list:
        df_c = pd.read_csv(i, sep=',', header=0)
        #    print(df_c['video_name'].tolist())
        # fr = i.values
        # print df_c
        df = df.append(df_c)
        # print df
        print('写入成功！')
        output_Archive = pd.DataFrame(df)
        # print outPath+item + '.csv'
        output_Archive.to_csv(outPath+item + '.csv')
        print('写入完毕！')

    print('3秒钟自动关闭程序！')
    time.sleep(3)

for item in txt:
    csvPath = basicPath + item
    print csvPath
    os.chdir(csvPath)
    combine(item)