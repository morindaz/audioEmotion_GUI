# coding=utf-8
'''
拼接54个已经合并的csv变成一个整体
'''
import os
import time
import glob
import pandas as pd
import numpy as np
basicPath = "C:\\Users\\Mypc\\Desktop\\morindaz\\audios\\csvFeature"   #54个csv的路径
outPath = "C:\\Users\\Mypc\\Desktop\\morindaz\\audios\\combine50"     #拼接完csv的输出路径
os.chdir(basicPath)
csvx_list = glob.glob('*.csv')
print('总共发现%s个CSV文件' % len(csvx_list))
time.sleep(2)
print('正在处理............')
df = pd.DataFrame()
flag = 0
for i in csvx_list:
    df_c = pd.read_csv(i, sep=',', header=0)
    #    print(df_c['video_name'].tolist())
    # fr = i.values
    # print df_c
    df_c['label']= np.array([flag] * len(df_c.values))
    flag = flag+1
    df = df.append(df_c)
    print df
    print('写入成功！')
    output_Archive = pd.DataFrame(df)
    output_Archive.to_csv(outPath+'combinedAll.csv')
    print('写入完毕！')

print('3秒钟自动关闭程序！')
time.sleep(3)

