# encoding: UTF-8
'''
可以提取到cmd的文字，送到audioExtract中进行处理
'''

import subprocess
import os
import threading
import Queue
import re
from plotEmotions import *
import matplotlib.pyplot as plt
# from '../main/pamarators' import *
update =""
emodbList = []
emodbProb = []
abcAffectList =[]
abcAffectProb =[]

def runCMD(cmd):
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1000)


def enqueue_output(out, queue):
    print "helllo"
    for line in iter(out.readline, b''):  #逐行读取cmd中的内容
        queue.put(line) #将命令放到队列中
    out.close() #将stderr关闭


def parser(line):
    if line.find('prob. class'):
        pass

def parseLine(line):
    flag = False
    if line.find('prob. class') > 0:
        flag = True
    return flag

def extractProb(line):
    pattern = re.compile('\'(.*)\'')
    key = pattern.findall(line)
    _, value = line.split(':')
    return key[0], value

label_emo = []
label_aff = []

def parseData(fig,line,note):
    global update, emodbList, emodbProb, abcAffectList, abcAffectProb
    # line1 = '     prob. class \'agresive\':0.222'
    print line
    key, value = extractProb(line)
    if note =="emodb":
        emodbList.append(key)
        emodbProb.append(value.strip())
    elif note =="abcAffect":
        abcAffectList.append(key)
        abcAffectProb.append(value.strip())
    print key, value

    if key == 'tired':
        update = True
    if update:
        showResults(fig, emodbProb, emodbList, abcAffectProb, abcAffectList)
        if len(emodbProb) > 0:
            plt.show()
            plt.pause(0.4)
        #
        # plt.show()
        # plt.pause(0.4)
        #置空操作
        emodbList = []
        emodbProb = []
        abcAffectList = []
        abcAffectProb = []
        update = False

def rotateSix(fig, q,note):
    time = ""
    if note =='emodb':
        time = 7
    elif note =='abcAffect':
        time = 6
    for cmd in range(time):
        lineInner = q.get_nowait()
        lineInner = lineInner.strip('\n')
        label = parseLine(lineInner)  # 这里的label有用吗
        print label
        if label:
            parseData(fig, lineInner, note)


# 主线程开始
def getCMD():
    os.chdir('E:/pingan/audioEmotion/opensmile/opensmile-2.3.0/opensmile-2.3.0/bin/Win32')
    cmd = 'SMILExtract_ReleasePortaudio -C E:\pingan\\audioEmotion\opensmile\opensmile-2.3.0\opensmile-2.3.0\config\emobase_live4.conf'
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    q = Queue.Queue()
    t = threading.Thread(target=enqueue_output, args=(child.stderr, q))
    # t.daemon = True # thread dies with the program
    t.start()
    # out =[]
    global update, emodbList, emodbProb, abcAffectList, abcAffectProb
    fig = plt.figure()  #主程序创建一张图
    plt.ion()
    while True:  #获取每一条数据
        try:
            line = q.get_nowait()  # or q.get(timeout=.1)
            if line.find("LibSVM  'emodbEmotion'") > 0:
                emodbEmotion = re.findall(r"~~> (.+?) <~~", line)
                # emodbList.append(emodbEmotion)
                print "here is emodb"
                rotateSix(fig, q,"emodb")
            elif line.find("LibSVM  'abcAffect'") > 0:
                print line
                abcAffect = re.findall(r"~~> (.+?) <~~", line)
                print "here is abcAffect"
                rotateSix(fig, q,"abcAffect")
            # plt.show()
            # plt.pause(0.5)

        except:
            continue
        # parse
        print "+++++"
        print line
        print emodbList
        print emodbProb
        print abcAffectList
        print abcAffectProb



