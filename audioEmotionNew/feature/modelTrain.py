# encoding:UTF-8
# import h5py
'''
ModelTrain 负责训练SVM分类器
通过gridSearch寻找模型最优参数
'./param.pkl'  './estimator.model' 保存了最优参数以及模型
'''
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
import pandas as pd
from sklearn.metrics import accuracy_score
import pyttsx

# from featureSelectSFS import get_data, featureSelectionSFS
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# rootdir = '/Users/fwei/pingan/audioExtract'


# 自定义打分函数
def scoring_method(y_true, y_pred, pos_label=1):
    return recall_score(y_true, y_pred, pos_label=pos_label,average='weighted')

# 画出分类器预测的分布图 (by Afei)
def plotDist(x, y, path):
    plt.style.use('bmh')
    plt.hist(x, color='teal', bins=20, normed=True, alpha=0.6)
    plt.hist(y, color='darkred', bins=20, normed=True, alpha=0.6)
    plt.legend(['no risk', 'has risk'])
    plt.savefig(path +'/dist.png', dpi=300, format='png')
    plt.ylabel('frequency')
    plt.xlabel('linear_svm result')

# 训练模型
def trainModel(X_train, y_train, scale_flag, weight, penalty, C, max_iter):
    x_size, feature_size = X.shape
    print('==== Current Feature Size:%d.' % feature_size)
    if scale_flag:
        mms = preprocessing.StandardScaler()
        X_train_scaled = mms.fit_transform(X_train)
        # X_test_scaled = mms.transform(X_test)
    else:
        X_train_scaled = X_train
        # X_test_scaled = X_test

    # Method #1
    param_gridA = {'linearsvc__C':C,
                   'linearsvc__penalty': penalty,
                   'linearsvc__max_iter': max_iter}
    pipeA = pipeline.make_pipeline(preprocessing.StandardScaler(), LinearSVC(dual=False,class_weight=weight))
    # 产生指定数量的独立的train/test数据集划分, 首先对样本全体打乱, 然后划分出train／test对
    # 返回分层划分， 创建划分的时候要保证每一个划分中类的样本比例与整体数据集中的原始比例保持一致
    print(y_train)
    sss = StratifiedShuffleSplit(y_train, 3, test_size=0.3, random_state=0)
    print(sss)
    fscore = make_scorer(scoring_method, pos_label=1)
    # gsA = grid_search.GridSearchCV(pipeA, param_grid=param_gridA, scoring='roc_auc', cv=sss, n_jobs=-1)
    gsA = grid_search.GridSearchCV(pipeA, param_grid=param_gridA, scoring=fscore, cv=sss, n_jobs=1)
    gsA = gsA.fit(X_train_scaled, y_train)
    bestScore = gsA.best_score_
    best_params = gsA.best_params_
    best_estimator = gsA.best_estimator_
    print('==== The best parame is %s(with the score:%f).' %(best_params, bestScore))
    return best_params, best_estimator  #best_params,estimator.model
    # Method #2
    # PipeLine 包含着gridSearchCV节省了每次标准化
    # param_gridB = {'C': C, 'penalty': penalty, 'max_iter':max_iter}
    # pipeB = pipeline.make_pipeline(preprocessing.StandardScaler(),
    #                               grid_search.GridSearchCV(LinearSVC(), param_grid=param_gridB, refit=True))

    # model = LinearSVC(penalty=penalty, dual=False,class_weight=weight, C=C, max_iter=max_iter)

if __name__ =='__main__':

    feature_flag = False
    param_flag = False
    # path1 = '.\\NoiseemotionSix4973.csv'
    # path1 = '.\\noiseCSV\\751Noise7Emo.csv'
    # path1 = '.\\noiseCSV\\NoiseemotionSix4374.csv'
    path1 = '.\\4374clearSixEmotions.csv'
    # featurePath = 'E:\\pingan\\audioEmotion\\audioEmotionNew\\feature\\selectedMorindaz.csv'
    df = pd.read_csv(path1, sep=',', header=0)
    data_F = df.values
    print len(data_F)
    # feature = pd.read_csv(featurePath, sep=',', header=0)
    # featureList = feature.values[:,1] #featureList记录了被选择出来的最优特征
    # print featureList
    # cv=0 withNoise
    # featureList = [128, 0,2, 235, 5, 6, 1, 8, 9, 10, 13, 14, 15, 16, 17, 658, 662, 25, 90, 543, 18, 165, 7, 530, 562, 258,
    #                121, 59, 70, 957]

    # cv=5 withNoise
    featureList=[0,1,2,5,6,7,8,9,10,13,14,15,16,17,786,974,121,153,91,348,479,70,18,494,495,496,499,500,457,697]
    featureList = featureList[0:21]
    # cv=0 clear
    # featureList = [128,0,2,708,389,1,202,62,268,847,976,81,83,505,5,33,419,65,177,616,107,45,559,49,436,565,182,311,377,446]

    print len(featureList)

    X = data_F[:, featureList]
    X = preprocessing.scale(X)
    Y = data_F[:, -1]
    Y = map(int, Y)
    Y = np.array(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    mms = preprocessing.StandardScaler()
    X_train = mms.fit_transform(X_train)
    X_test = mms.transform(X_test)

    # Params List
    weightRange = [dict(zip(range(0, 2), (1, values))) for values in range(14, 24)]
    print weightRange

    cRange = np.logspace(0, 2, 6)
    penaltyRange = ['l1', 'l2']
    maxIterRange= np.logspace(2, 4, 5)
    myfile = os.path.exists('./param.pkl')
    if myfile:
        param_flag = True
        print('==== 参数最优化已经存在.')

    if not param_flag:
        scaled_flag = False
        # best_params, model = trainModel(X_train, y_train, scaled_flag, weight=weightRange, C=cRange, penalty=penaltyRange, max_iter=maxIterRange)
        best_params, model = trainModel(X_train, y_train, scaled_flag, weight='balanced', C=cRange, penalty=penaltyRange, max_iter=maxIterRange)
        # 保存模型参数
        # with h5py.File('best_params.h5','w') as handler:
        #     handler.create_dataset('best_param', data=best_params)
        joblib.dump(best_params,'./param.pkl')
        joblib.dump(model, './estimator.model')
    param = None
    # 从文件读取LinearSVC最佳参数设定
    clf = joblib.load('./estimator.model')
    param = joblib.load('./param.pkl')
    # linearsvc classifier
    print(clf)
    print 1111111111111111111
    print param
    stddc = clf.named_steps['standardscaler']
    model = clf.named_steps['linearsvc']
    print(model.coef_)
    # Bring features onto the same scale
    # print(X_train_scaled)
    # 样本外测试
    y_pred = clf.predict(X_test)
    recall_score_0 = recall_score(y_test, y_pred, pos_label=0,average='weighted')
    recall_score_1 = recall_score(y_test, y_pred, pos_label=1,average='weighted')
    # precision_score = precision_score(y_test, y_pred, pos_label=0)
    # roc_auc_score = roc_auc_score(y_test, y_pred,average='weighted')
    # confusion_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1])
    # print('==== Out-sample recall(0):%s, out-sample recall(1):%s' % (recall_score_0, recall_score_1))
    # print('==== The Roc-Auc-Score:%f' % roc_auc_score)
    print('==== The Confuse-Matrix is:%s' % confusion_matrix)
    acc = accuracy_score(y_test, y_pred)
    # count = 0
    # for i in range(len(y_pred)):
    #     if y_pred[i]==y_test[i]:
    #         count = count+1
    # print len(y_pred)
    # print('==== The Count is:%s' % count)
    print('==== The Accuracy is:%s' % acc)
    # pos_1 = np.argwhere(y_test==1)
    # print(np.sum(y_pred[pos_1])/ np.sum(y_test))
    print(model.intercept_)
    engine = pyttsx.init()
    engine.say('Congratulations!')
    engine.runAndWait()
    # # 画图显示预测分布
    # path = ".//"
    # multiply_result = np.zeros((len(y_test)))
    # X_test = stddc.transform(X_test)
    # for i in range(len(y_test)):
    #     multiply_result[i] = np.dot(model.coef_, X_test[i, :]) + model.intercept_
    #     print "hello"
    # x_plot = multiply_result[y_test == 0]
    # y_plot = multiply_result[y_test == 1]
    # print(x_plot)
    # print(y_plot)
    # plotDist(x_plot, y_plot, path)


