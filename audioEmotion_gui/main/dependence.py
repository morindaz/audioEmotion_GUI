# coding=utf-8
'''
主文件需加载的依赖文件
'''

import sys
import os
import threading
import atexit
import pyaudio
from pyaudio import PyAudio, paInt16
from datetime import datetime
import wave
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import figure
from PyQt4 import QtGui, QtCore
from parameters import *
from MicrophoneRecorder import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
