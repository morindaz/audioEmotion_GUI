'''
seems to be useless
'''

# coding=utf-8
# import sys
# from PyQt4 import QtGui
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
#
#         self.setToolTip('This is a <b>QWidget</b> widget')
#         btn = QtGui.QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#         qbtn = QtGui.QPushButton('Quit', self)
#         qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Tooltips')
#         self.show()
#
# def main():
#
#     app = QtGui.QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()




##############
import sys
from pyaudio import PyAudio, paInt16
from datetime import datetime
import wave
import numpy as np
from PyQt4 import QtGui, QtCore
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
# matplotlib对PyQt4的支持
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# define of params
# NUM_SAMPLES = 2000
# framerate = 8000
# channels = 1
# sampwidth = 2
# # record time
# TIME = 10
#
#
# class audioEmotion(QtGui.QMainWindow):
#
#     def __init__(self):
#         super(audioEmotion, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#
#         button1 = QtGui.QPushButton("Record", self)
#         button1.move(80, 190)
#
#         button2 = QtGui.QPushButton("Analyze", self)
#         button2.move(290, 190)
#
#
#         self.connect(button1, QtCore.SIGNAL('clicked()'),
#             self.buttonClicked)
#         self.connect(button1, QtCore.SIGNAL('clicked()'),
#             self.record_wave)
#
#         self.connect(button2, QtCore.SIGNAL('clicked()'),
#             self.buttonClicked)
#
#         self.statusBar().showMessage('Ready')
#         self.setWindowTitle('AudioEmotion_gui')
#         self.resize(490, 300)
#
#     def buttonClicked(self):
#         sender = self.sender()
#         if sender.text()=='Analyze':  # 判断单选按钮是否被选中
#             print("stream test start")
#             self.statusBar().showMessage(sender.text() + ' was pressed')
#
#     def save_wave_file(self,filename, data):
#         '''''save the date to the wav file'''
#         wf = wave.open(filename, 'wb')
#         wf.setnchannels(channels)
#         wf.setsampwidth(sampwidth)
#         wf.setframerate(framerate)
#         wf.writeframes("".join(data))
#         wf.close()
#
#     def record_wave(self):
#         # open the input of wave
#         pa = PyAudio()
#         stream = pa.open(format=paInt16, channels=1,
#                          rate=framerate, input=True,
#                          frames_per_buffer=NUM_SAMPLES)
#         save_buffer = []
#         count = 0
#         while count < TIME * 4:
#             # read NUM_SAMPLES sampling data
#             string_audio_data = stream.read(NUM_SAMPLES)
#             save_buffer.append(string_audio_data)
#             count += 1
#             print '.'
#
#         filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
#         self.save_wave_file(filename, save_buffer)
#         save_buffer = []
#         print filename, "saved"
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     ex = audioEmotion()
#     ex.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()