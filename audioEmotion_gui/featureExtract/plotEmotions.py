# coding=utf-8
'''
负责画图展示分析出的两个情绪结果
可以处理online 和 offline
'''

import numpy as np
from matplotlib import pyplot as plt
def showResults(fig,data_emo, label_emo, data_aff, label_aff):
    fig.clear()
    #第一幅图
    ax1 = fig.add_subplot(2,1,1)  #两行一列的图片
    len_emo = len(label_emo) #取出emo的长度
    x = np.arange(len_emo) #生成一个长度为emo的序列
    width = 1 / 2.0  #定义宽度,还是列的坐标
    plt.bar(x + width / 2, data_emo, width / 2) #开始位置，
    ax1.set_xticks(x + width / 2.0)
    ax1.set_xticklabels(label_emo)
    #第二幅图
    ax2 = fig.add_subplot(2,1,2) #画第二幅图
    len_aff = len(label_aff) #affection
    x = np.arange(len_aff)
    width = 1 / 2.0
    plt.bar(x + width / 2, data_aff, width / 2)
    ax2.set_xticks(x + width / 2.0)
    ax2.set_xticklabels(label_aff)
    fig.canvas.draw()
