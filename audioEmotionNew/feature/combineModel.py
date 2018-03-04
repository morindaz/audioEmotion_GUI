# coding=utf-8
import h5py
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn import pipeline
from sklearn import grid_search
import os
import numpy as np
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.externals import joblib
from sklearn.metrics import recall_score, precision_score, make_scorer, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
from featureSelectSFS import getCSVData
import pandas as pd
from sklearn.svm import LinearSVC

# path1 = 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\delwithLabel.csv'
path1 = 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\combinedwithLabel.csv'
# featurePath = 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\selectedMorindaz.csv'
df = pd.read_csv(path1, sep=',', header=0)
data_F = df.values
# feature = pd.read_csv(featurePath, sep=',', header=0)
# featureList = feature.values[:,1] #featureList记录了被选择出来的最优特征
# print featureList
featureList = [128,0,235,5,6,1,8,9,10,13,14,15,16,17,658,662,25,90,543,18,165,7,530,562,258,121,59,70,957]

selectedData = data_F[0:490,featureList]
selectedData = preprocessing.scale(selectedData)
label = data_F[0:490,-1]
label = map(int,label)
label = np.array(label)
# print featureList
# print label
# print len(selectedData)
# print selectedData
# LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
#      intercept_scaling=1, loss='squared_hinge', max_iter=1000,
#      multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
#      verbose=0)
clf = LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0)
clf.fit(selectedData, label)

# print(clf.coef_)
# print(clf.intercept_)
# print len(selectedData)
# print len(label)
# plotDist(selectedData, label, path)
result = []
correctItem = 0
for i in range(len(selectedData)):
    selectedDataTest = data_F[i, featureList]
    a = clf.predict(selectedDataTest.reshape((1,-1))) #predict要求传进去的是array之前传进去的是List
    result.append(a[0])
    if i>0 and i<165 and a[0]==0:
        correctItem = correctItem+1
    elif i>164 and i<278 and a[0]==1:
        correctItem = correctItem+1
    elif i>278 and i<490 and a[0]==2:
        correctItem = correctItem+1
print "The accuracy is "+str(float(correctItem)/len(result))
    # print(clf.predict(selectedDataTest))
print result
print len(result)
