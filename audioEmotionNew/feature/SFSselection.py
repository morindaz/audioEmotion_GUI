# coding=utf-8

from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import os
def SFSselect():
       path1= 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\delwithLabel.csv'
       # path2= 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\csv\\Admiration.csv'
       # path3= 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\csv\\Aggressiveness.csv'
       df1 = pd.read_csv(path1, sep=',', header=0)
       # df2 = pd.read_csv(path2, sep=',', header=0)
       # df3 = pd.read_csv(path3, sep=',', header=0)
       data = df1.values[:,0:-1]
       # data_accept2 = df2.values[:,2:-1]
       # print data_accept1
       # data_accept3 = df3.values
       # data = np.concatenate((data_accept1, data_accept2), axis=0)
       labelList = []
       print len(data)
       label = df1.values[:,-1]
       label = map(int,label)
       label = np.array(label)
       # 转换为arra
       print len(label)
       # for item in label:
       #        labelList.append(item)
       # print type(labelList)
       print label
       logi = LogisticRegression(C=0.5,penalty='l2',multi_class='multinomial',class_weight='balanced',solver='lbfgs')
       # logi = LogisticRegression(C=0.5,penalty='l2',class_weight='balanced')
       sfs1 = SFS(logi,
              k_features=30,
              forward=True,
              floating=False,
              verbose=2,
              cv=2,
              scoring='accuracy')


       sfs1 = sfs1.fit(data, label)
       a = sfs1.subsets_
       avalue = list(a.values())
       indexVal = avalue[-1]['feature_idx']
       _, audioname = os.path.split('Acceptance.csv')
       filestr, postfix = os.path.splitext(audioname)
       featureIdx = []
       for item in indexVal:
              featureIdx.append(item)
       print featureIdx
       outPut = {'Index': featureIdx}
       output_Archive = pd.DataFrame(outPut)
       output_Archive.to_csv('selectedMorindaz1.csv')


if __name__ == "__main__":
       SFSselect()
