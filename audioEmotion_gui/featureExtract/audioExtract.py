# encoding: UTF-8
'''
可以实时的提取数据
'''
import glob
import os
import subprocess
import re
from cmdInfoExtract import *
from plotEmotions import *
# from matplotlib import pyplot as plt

# def parseLine(line):
#     if line.find('prob. class') < 0:
#         return False
#     return True
#
# def extractProb(line):
#     pattern = re.compile('\'(.*)\'')
#     key =  pattern.findall(line)
#     _,value = line.split(':')
#     return key[0], value
#
# label_emo = []
# label_aff = []
#
#
# def parseData():
#     line1 = '     prob. class \'agresive\':0.222'
#     label = parseLine(line1) #这里的label有用吗
#     key, value = extractProb(line1)
#     print key, value
#     update = ""
#     if key == 'tired':
#         update = True
#     if update:
#         showResults()

if __name__ == '__main__':
    # 一个线程,持续读取Microphone声音并且cmd显示
    # t = threading.Thread(target=getCMD)
    # p = threading.Thread(target=parseData)
    # t.start()
    #另一个线程负责解析每一行的数据。如何让两个线程同时运行？
    # p.start()
    getCMD()
    # line1 = '     prob. class \'agresive\':0.222'
    # label = parseLine(line1)
    # key, value = extractProb(line1)
    # print key, value
    # update = ""
    # if key == 'tired':
    #     update = True
    # if update:
    #     showResults()
