# coding=utf-8
'''
分析每个wav音频文件并且将opensmile分析出的特征存成csv
批量分析,存成单独的csv。导出路径在"E:\\out"
需要存到对应文件夹下面，或者生成一个合并起来的csv
http://records.mlab.no/2015/01/05/opensmile-the-munich-open-source-large-scale-multimedia-feature-extractor-a-tutorial-for-version-2-1/
'''
import os

# opensmile Directory
openSmileDir = "E:\pingan\\audioEmotion\opensmile\opensmile-2.3.0\opensmile-2.3.0\\bin\Win32"
fconfig = 'E:\pingan\VoiceRecognize\opensmile\emobase_csv.conf'
inDir = "E:\\audio"
outDir = "E:\\out"
txt = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe',
       'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness',
       'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy',
       'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy',
       'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse',
       'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust',
       'Uneasiness', 'vitality']
# os.system('SMILExtract_Release -C E:\pingan\VoiceRecognize\opensmile\emobase_csv.conf -I E:\pingan\\audioEmotion_gui\\2017-08-22_13_02_16.wav -O ..\:Moaaa_feature.csv')


# def featureExtract(audioRoot, outdir, cmd, fconfig, outflag, output_postfix):
        # os.system(command)


if __name__ == '__main__':
    #存储第几个文件夹
    eachDir = txt[0]
    inMovovDir = inDir + "\\" + eachDir
    # print formatInDir
    #转到50中情绪对应的文件夹
    os.chdir(inMovovDir)
    #输出到featureDir
    featureDir = outDir+'\\feature'
    os.chdir(openSmileDir)

    # print formatInDir
    # outMovDir = outDir + "\\" + eachDir
    # cmd进入到对应文件夹
    os.chdir(inMovovDir)
    # 打开包含了某种情绪文件夹下所有wav的txt
    file = open(eachDir + '.txt')
    lines = file.readlines()
    formatLines = []
    for line in lines:
        line = line.strip('\n')
        formatLines.append(line)  # formatLines数组得到了目录下所有wav列表，并且去除了\n
    print formatLines
    os.chdir(openSmileDir)
    for line in formatLines:
        # 提取每个wav的名字，将名字和mov分开
        _, audioname = os.path.split(line)
        filestr, postfix = os.path.splitext(audioname)
        featurename = filestr + ".csv"
        item = inMovovDir + "\\" + line
        # os.system('SMILExtract_Release -C E:\pingan\VoiceRecognize\opensmile\emobase_csv.conf -I E:\pingan\\audioEmotion_gui\\2017-08-22_13_02_16.wav -O ..\:Moaaa_feature.csv')
        cmd = 'SMILExtract_Release -C ' + fconfig + " -I "+inMovovDir+"\\"+formatLines[0]+" -O "+outDir+"\\"+featurename
        print cmd
        os.system(cmd)
