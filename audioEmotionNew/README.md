# audioEmotionNew
平安通过语音特征提取，筛选提取特征 通过特征组合等方式判断出相对应的情绪
用gridSearchCv 选择最优模型参数
http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV
stacking wqo
------------------------------------------
5973条记录中  筛选4373条数据规则
编号(具体类别)-原数量  -删除的数量 = 最后的数量(删除开始-删除结束行数)
0(sadness)-1524  -600 =924(2-601)
1(fear)-543
2(surprise)-327
3(joy)-1700  -800=900(1796-2595)
4(anger)-762
5(disgust)-1117  -200=917(3458-3657)

400条数据 小分类
noise
delWithLabel cv=0 44.7%   
delWithLabel cv=5 39.837398374%

clear(withOutNoise)
delete cv=0  46.3414634146%
——————————————————————
5793条数据 6大分类
6Emotions:
clear: 0.315261044177
noise: 0.326639892905
______________________
4374行数据，6大分类，按筛选4374条数据规则
clear:0.270566727605
noise:0.267824497258
特征筛选 
noise23个特征最优结果
noise:0.212065813528(10个特征)
noise:0.229433272395(15个特征)
noise:0.269652650823(20个特征)
noise:0.267824497258(22个特征)
***noise:0.270566727605(23个特征)***
noise:0.26873857404(24个特征)
noise:0.267824497258(30个特征)

clear 22个特征最优结果
clear:0.26508226691(21个特性)
***clear:0.271480804388(22个特征)***
clear:0.270566727605(23个特征)
——————————————————————
4099行数据(5个大分类)
clear 0.491707317073
noise 0.483902439024
______________________
751行数据(7个小分类 sadness\fear\surprise\joy\anger\disgusst\contemp)
clear:0.186170212766
24个特征最优结果
noise:0.202127659574 (30个特征)
noise:0.202127659574 (25个特征)
***noise:0.228723404255 (24个特征)***
noise:0.218085106383 (23个特征)
noise:0.212765957447 (20个特征)
noise:0.186170212766 (15个特征)
noise:0.143617021277 (10个特征)

persiveness小类别会变成 Neutral大类
按照文章reading what the mind thinks from将54种情绪分到6类别中。
但是17(depression->1\) 22(embarrassed->2\) 27(grievance->1\) 45(shame->1\)
具体六个类别为
1\sadness (43,24,35,50,37,9,21,6,52,42,47,17,27,45)
2\fear(25,41,14,7,22)
3\surprise(5,48,32)
4\joy(33,34,36,1,26,18,46,53,51,0,28,44,11,8,40)
5\anger(10,16,13,15,29,2,3)
6\disgust(20,30,4,23,49,39,19,38,12,31)
(neutral)属于一个大类，下面还没有数据。persiveness现在还有，之后会删除


(0, 'Acceptance')
(1, 'Admiration')
(2, 'Aggressiveness')
(3, 'Angry')
(4, 'Annoyance')
(5, 'Anticipation')
(6, 'Apprehension')
(7, 'Awe')
(8, 'Boastfulness')
(9, 'Boredom')
(10, 'Bravery')
(11, 'Calm')
(12, 'Conflict')
(13, 'Contempt')
(14, 'Cowardice')
(15, 'Deceptiveness')
(16, 'Defiance')
(17, 'Depression')
(18, 'Desire')
(19, 'Disapproval')
(20, 'Disgust')
(21, 'Distraction')
(22, 'Embarrassed')
(23, 'Envy')
(24, 'Fatigue')
(25, 'Fear')
(26, 'Gratitude')
(27, 'Grievance')
(28, 'Harmony')
(29, 'Hate')
(30, 'Insincerity')
(31, 'Insult')
(32, 'Interest')
(33, 'Joy')
(34, 'Love')
(35, 'Neglect')
(36, 'Optimism')
(37, 'Passiveness')
(38, 'Pensiveness')
(39, 'Pessimism')
(40, 'Pride')
(41, 'Puzzlement')
(42, 'Remorse')
(43, 'Sadness')
(44, 'Serenity')
(45, 'Shame')
(46, 'Sincerity')
(47, 'Submission')
(48, 'Surprise')
(49, 'Suspicion')
(50, 'Tension')
(51, 'Trust')
(52, 'Uneasiness')
(53, 'vitality')
=======
love
joy
anger
contempt
surprise
fear
sadness
