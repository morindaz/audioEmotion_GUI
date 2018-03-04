# AudioEmotion GUi  -Designed by Morindaz

#Todo
50种情绪的音频提取和预处理（5）;
2.软件中用queue，把录入的音频文件名存queue, 然后另一线程从队列取文件预测结果（3）；

1. Stop功能，自主选择录音停止时间，现在停止会导致异常
2. 文件调用os接口用字符串拼接，改成方便修改的目录
3. 分析频谱的Pyqtgraph加入
4. csv中分析音频列表，变成多行数据输出，多个样本
5. 通过List分析,如果有新保存的wmv,则读取并且分析频谱


#Notes and Finished Log

- 执行入口文件 python AudioEmotion.py
- 实时读取麦克风并显示频谱
- 点击Record能够录音大约4秒时间
- 点击Analysis能够调用opensmile输出csv文档
---


#Dependicies
1. PyQT4 

---
#Tutorials
1. https://www.tutorialspoint.com/pyqt/pyqt_quick_guide.htm

#Useful Links
1. http://amyboyle.ninja/Pyqtgraph-live-spectrogram
2. http://flothesof.github.io/pyqt-microphone-fft-application.html
3. http://records.mlab.no/2015/01/05/opensmile-the-munich-open-source-large-scale-multimedia-feature-extractor-a-tutorial-for-version-2-1/
