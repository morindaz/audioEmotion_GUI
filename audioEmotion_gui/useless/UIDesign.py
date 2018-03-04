# from dependence import *
# class MplFigure(object):
#     def __init__(self, parent):
#         self.figure = figure.Figure(facecolor='white')
#         self.canvas = FigureCanvas(self.figure)
#         # self.toolbar = NavigationToolbar(self.canvas, parent)
#         self.toolbar = NavigationToolbar(self.canvas, parent)
#
# class LiveFFTWidget(QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#
#         # customize the UI
#         self.initUI()
#
#         # init class data
#         self.initData()
#
#         # connect slots
#         self.connectSlots()
#
#         # init MPL widget
#         self.initMplWidget()
#
#     def initUI(self):
#         #绘图文字区域：Auto gain for frequency spectrum
#         hbox_gain = QtGui.QHBoxLayout()
#         autoGain = QtGui.QLabel('Auto gain for frequency spectrum')
#         autoGainCheckBox = QtGui.QCheckBox(checked=True)
#         hbox_gain.addWidget(autoGain)
#         hbox_gain.addWidget(autoGainCheckBox)
#         #增加Record Button
#         w = QtGui.QWidget()
#         Rec = QtGui.QPushButton(w)
#         Rec.setText("Record")
#         hbox_gain.addWidget(Rec)
#         self.connect(Rec, QtCore.SIGNAL('clicked()'),
#                      self.record_wave)
#         # 增加Stop Button
#         stop = QtGui.QWidget()
#         self.Stop = QtGui.QPushButton(stop)
#         self.Stop.setText("Stop")
#         hbox_gain.addWidget(self.Stop)
#         self.connect(self.Stop, QtCore.SIGNAL('clicked()'),
#                      self.stop_wave)
#         # 增加Analysis Button
#         Analysis = QtGui.QPushButton(w)
#         Analysis.setText("Analysis")
#         hbox_gain.addWidget(Analysis)
#         self.connect(Analysis, QtCore.SIGNAL('clicked()'),
#                      self.analysis_data)
#
#         # reference to checkbox
#         self.autoGainCheckBox = autoGainCheckBox
#         #Manual gain level for frequency spectrum文字区域
#         hbox_fixedGain = QtGui.QHBoxLayout()
#         fixedGain = QtGui.QLabel('Manual gain level for frequency spectrum')
#         fixedGainSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
#         hbox_fixedGain.addWidget(fixedGain)
#         hbox_fixedGain.addWidget(fixedGainSlider)
#         self.fixedGainSlider = fixedGainSlider
#         vbox = QtGui.QVBoxLayout()
#         vbox.addLayout(hbox_gain)
#         vbox.addLayout(hbox_fixedGain)
#
#         # mpl figure
#         self.main_figure = MplFigure(self)
#         vbox.addWidget(self.main_figure.toolbar)
#         vbox.addWidget(self.main_figure.canvas)
#         self.setLayout(vbox)
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('AudioEmotion')
#         self.show()
#         # timer for calls, taken from:
#         # http://ralsina.me/weblog/posts/BB974.html
#         timer = QtCore.QTimer()
#         timer.timeout.connect(self.handleNewData)
#         timer.start(50)
#         # keep reference to timer
#         self.timer = timer
#         self.resize(690, 550)
#
#     def initData(self):
#         mic = MicrophoneRecorder()
#         mic.start()
#
#         # keeps reference to mic
#         self.mic = mic
#
#         # computes the parameters that will be used during plotting
#         self.freq_vect = np.fft.rfftfreq(mic.chunksize,
#                                          1./mic.rate)
#         self.time_vect = np.arange(mic.chunksize, dtype=np.float32) / mic.rate * 1000
#
#     def connectSlots(self):
#         pass
#
#     def initMplWidget(self):
#         """creates initial matplotlib plots in the main window and keeps
#         references for further use"""
#         # top plot
#         self.ax_top = self.main_figure.figure.add_subplot(211)
#         self.ax_top.set_ylim(-32768, 32768)
#         self.ax_top.set_xlim(0, self.time_vect.max())
#         self.ax_top.set_xlabel(u'time (ms)', fontsize=6)
#
#         # bottom plot
#         self.ax_bottom = self.main_figure.figure.add_subplot(212)
#         self.ax_bottom.set_ylim(0, 1)
#         self.ax_bottom.set_xlim(0, self.freq_vect.max())
#         self.ax_bottom.set_xlabel(u'frequency (Hz)', fontsize=6)
#         # line objects
#         self.line_top, = self.ax_top.plot(self.time_vect,
#                                          np.ones_like(self.time_vect))
#
#         self.line_bottom, = self.ax_bottom.plot(self.freq_vect,
#                                                np.ones_like(self.freq_vect))
#
#
#     def handleNewData(self):
#         """ handles the asynchroneously collected sound chunks """
#         # gets the latest frames
#         frames = self.mic.get_frames()
#         if len(frames) > 0:
#             # keeps only the last frame
#             current_frame = frames[-1]
#             # plots the time signal
#             self.line_top.set_data(self.time_vect, current_frame)
#             # computes and plots the fft signal
#             fft_frame = np.fft.rfft(current_frame)
#             if self.autoGainCheckBox.checkState() == QtCore.Qt.Checked:
#                 fft_frame /= np.abs(fft_frame).max()
#             else:
#                 fft_frame *= (1 + self.fixedGainSlider.value()) / 5000000.
#                 #print(np.abs(fft_frame).max())
#             self.line_bottom.set_data(self.freq_vect, np.abs(fft_frame))
#
#             # refreshes the plots
#             self.main_figure.canvas.draw()
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
#     def analysis_data(self):
#         global featureDir
#         audioRoot = '2017-08-22_13_02_16.wav'
#         featureDir = baseDir + '\\feature'
#         # featureDir = 'E:\pingan\\audioEmotion_gui\\feature'
#         os.chdir(openSmileDir)
#         cmd = 'SMILExtract_Release -C E:\pingan\VoiceRecognize\opensmile\{0} -I {1} {2} {3}\{4}'
#         fconfig = 'emobase_csv.conf'
#         featurename = '.csv'
#         self.featureExtract(audioRoot, featureDir, cmd, fconfig, outputflag, featurename)
#
#
#     def stop_wave(self):
#         global Flag
#         Flag = False
#
#     def start_record(self):
#         global Flag, itemList
#         save_buffer = []
#         pa = PyAudio()
#         stream = pa.open(format=paInt16, channels=1,
#                          rate=framerate, input=True,
#                          frames_per_buffer=NUM_SAMPLES)
#         count = 0
#         while count < TIME * 4 and Flag:
#             # read NUM_SAMPLES sampling
#             string_audio_data = stream.read(NUM_SAMPLES)
#             save_buffer.append(string_audio_data)
#             count += 1
#             print '.'
#             if Flag == False:  # 判断Stop是否被按下
#                 print("Already Stopped")
#
#         filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
#         self.save_wave_file(filename, save_buffer)
#         save_buffer = []
#         itemList.append(filename)
#         print filename, "saved"
#         print itemList
#
#     def record_wave(self):
#         global Flag
#         Flag = True
#         # open the input of wave
#         t = threading.Thread(target=self.start_record)
#         t.start()
#
#     def featureExtract(self,audioRoot, outdir, cmd, fconfig, outflag, output_postfix):
#         featurename = "Moaaaaaaaa_feature" + output_postfix
#         item = baseDir + "\\" + "2017-08-22_13_02_16.wav"
#         command = cmd.format(fconfig, item, outputflag, featureDir, featurename)
#         os.system(command)