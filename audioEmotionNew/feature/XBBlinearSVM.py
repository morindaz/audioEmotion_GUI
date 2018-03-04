# coding=utf-8
from sklearn.svm import LinearSVC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.datasets import make_classification
from sklearn import preprocessing
# X, y = make_classification(n_features=4, random_state=0)

path = "E:\\pingan\\audioEmotion\\audioEmotionNew"
def plotDist(x, y, path):
    plt.style.use('bmh')
    plt.hist(x, color='teal', bins=20, normed=True, alpha=0.6)
    plt.hist(y, color='darkred', bins=20, normed=True, alpha=0.6)
    plt.legend(['no risk', 'has risk'])
    plt.savefig(path +'/dist.png', dpi=300, format='png')
    plt.ylabel('frequency')
    plt.xlabel('linear_svm result')

path1 = 'delwithLabel.csv'
# path1 = 'combinedwithLabel.csv'
df = pd.read_csv(path1, sep=',', header=0)
data_F = df.values
# feature = pd.read_csv(featurePath, sep=',', header=0)
# featureList = feature.values[:,1] #featureList记录了被选择出来的最优特征
# print featureList
featureList = [128,0,235,5,6,1,8,9,10,13,14,15,16,17,658,662,25,90,543,18,165,7,530,562,258,121,59,70,957]

# selectedData = data_F[:,featureList]
# label = data_F[:, -1]

selectedData = data_F[0:490,featureList]
label = data_F[0:490,-1]

selectedData = preprocessing.scale(selectedData)

# label = map(int,label)
label = np.array(label, dtype='int64')

print(selectedData.shape)
print(label.shape)
# LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
#      intercept_scaling=1, loss='squared_hinge', max_iter=1000,
#      multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
#      verbose=0)
clf = LinearSVC(C=1.0, class_weight=None, dual=False, fit_intercept=True,
     intercept_scaling=11, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l1', random_state=0, tol=0.0001,
     verbose=0)

clf.fit(selectedData, label)
print selectedData

accuracy = clf.predict(selectedData)
print('accuracy:', (float(sum(accuracy == label)) / accuracy.shape[0]))