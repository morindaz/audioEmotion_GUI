# coding=utf-8
'''
opensmile离线分析有五种情绪。
利用正则提取出相关的参数，给直方图提供数据，这里可以画出相关的图片
'''

import re
import pandas as pd
from plotEmotions import *
import matplotlib.pyplot as plt

file = open('E:\\sss.txt')


lines = file.readlines()
emo1 = lines[4]  # Category,anger,boredom,digust,fear,happiness,neutral,sadness
emo2 = lines[5]  # Category,aggressiv,cheerful,intoxicated,nervous,neutral,tired
emo3 = lines[6]
print emo1
# catPat1 = '(?<CATEGORY=).*?(?=::)'

# proceed emo1
category1 = re.findall(r"CATEGORY=(.+?)::", emo1)  #
anger = re.findall(r"anger:(.+?)::", emo1)  #
boredom = re.findall(r"boredom:(.+?)::", emo1)
disgust = re.findall(r"disgust:(.+?)::", emo1)
fear = re.findall(r"fear:(.+?)::", emo1)
happiness = re.findall(r"happiness:(.+?)::", emo1)
neutral_1 = re.findall(r"neutral:(.+?)::", emo1)
sadness = re.findall(r';sadness:(.+?)$', emo1)
# print sadness
# sadness = 2

# proceed emo2
category2 = re.findall(r"CATEGORY=(.+?)::", emo2)  #
agressiv = re.findall(r"agressiv:(.+?)::", emo2)  #
cheerful = re.findall(r"cheerful:(.+?)::", emo2)  #
intoxicated = re.findall(r"intoxicated:(.+?)::", emo2)  #
nervous = re.findall(r"nervous:(.+?)::", emo2)  #
neutral_2 = re.findall(r"neutral:(.+?)::", emo2)  #
tired = re.findall(r';tired:(.+?)$', emo2)
# tired = 3
outPut1 = {'anger': anger, 'boredom': boredom, 'disgust': disgust, 'fear': fear,
           'happiness': happiness, 'neutral': neutral_1, 'sadness': sadness}
outPut2 = { 'agressiv': agressiv, 'cheerful': cheerful, 'intoxicated': intoxicated,
           'nervous': nervous, 'neutral': neutral_2, 'tired': tired}

emotions = pd.DataFrame(outPut1)
emotions = emotions.convert_objects(convert_numeric=True)
affections = pd.DataFrame(outPut2).convert_objects(convert_numeric=True)
# output1.to_csv('output1.csv')
# output2.to_csv('output2.csv')
print emotions
print affections

label_e = list(emotions.columns)
label_a = list(affections.columns)
# print label_e
# print label_a

data_e = emotions.values
data_a = affections.values
# print data_e
# print data_a

fig = plt.figure()
# showResults(fig,data_e[0], label_e, data_a[0], label_a)
plt.pause(1)
showResults(fig, data_a[0], label_a,data_e[0], label_e)
plt.show()