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

# cv=5 withNoise
featureList = [0, 1, 2, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 786, 974, 121, 153, 91, 348, 479, 70, 18, 494, 495, 496,
               499, 500, 457, 697]
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