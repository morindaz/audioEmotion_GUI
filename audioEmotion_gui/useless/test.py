# # coding=utf-8
# import os
#
# #opensmile的路径
# openSmileDir = "E:\\pingan\\VoiceRecognize\\opensmile\\opensmile-2.3.0\\opensmile-2.3.0\\bin\\Win32"
# baseDir = "E:\pingan\\audioEmotion_gui"
# # os.system('SMILExtract_Release -C E:\pingan\VoiceRecognize\opensmile\emobase_csv.conf -I E:\pingan\\audioEmotion_gui\\2017-08-22_13_02_16.wav -O ..\:Moaaa_feature.csv')
# def featureExtract(audioRoot, outdir, cmd, fconfig, outflag, output_postfix):
#     featurename = "Moaaaaaaaa_feature"+output_postfix
#     item = baseDir+"\\"+"2017-08-22_13_02_16.wav"
#     command = cmd.format(fconfig, item, outputflag, featureDir,featurename)
#     os.system(command)
#
# if __name__ == '__main__':
#
#     audioRoot = '.\\2017-08-22_13_02_16.wav'
#     print audioRoot
#     featureDir = baseDir+'\\feature'
#     # featureDir = 'E:\pingan\\audioEmotion_gui\\feature'
#     os.chdir(openSmileDir)
#     # cmd2 = '/Users/fwei/pingan/audioExtract/dataset/bin/SMILExtract -C /Users/fwei/pingan/audioExtract/dataset/config/{0} -I {1} {2} {3}/{4}'
#     cmd = 'SMILExtract_Release -C E:\pingan\VoiceRecognize\opensmile\{0} -I {1} {2} {3}\{4}'
#     fconfig = 'emobase_csv.conf'
#     outputflag = '-O'
#     featurename = '.csv'
#     featureExtract(audioRoot, featureDir, cmd, fconfig, outputflag, featurename)
