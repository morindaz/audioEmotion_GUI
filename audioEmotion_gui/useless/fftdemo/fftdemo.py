# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import numpy as N
#import scipy as S

from ui_main import Ui_Form

from pylab import *

class Plot_Widget(QWidget,  Ui_Form):
    def __init__(self, data2plot=None, parent = None):
        super(Plot_Widget, self).__init__(parent)
        self.setupUi(self)
        
        QObject.connect(self.plotBtn, SIGNAL("clicked()"),self.plotData)
        QObject.connect(self.save_figure_Button,SIGNAL('clicked()'),self.plotWidget.toolbar.save_figure)


        QObject.connect(self.getdata_Button,SIGNAL('clicked()'),self.getdata)
        
    def getdata(self):
        ncount = eval(str(self.samplepoint.text())) #采样点数
        Fs = eval(str(self.samplefreq.text()))#获取采样频率
        Ts=1./Fs#采样间隔时间

        sampleTime = Ts*ncount#采样持续时间

        x = linspace(0,sampleTime,ncount)#时域波形x轴坐标


        func1=eval(str(self.funcexp.text()))
        self.data1.setText(str(func1))

        fftdatastr=str(self.data1.toPlainText())  #调整格式 以便识别
        fftdatastr1=fftdatastr[1:-1]
        fftdatastr1=fftdatastr1.split()
        fftdatastr1=str(fftdatastr1).replace('\'','')
        self.data1.setText(str(eval(fftdatastr1)))
        self.sample_period_time.setText(str(1./Fs))
        #print Fs



    def plotData(self):

       


        fftsize=eval(str(self.comboBox.currentText()))  #currentText返回的是QString类型，需要转换
        fftdata=eval(str(self.data1.toPlainText()))



        freq =  arange(0, fftsize)  # x ticks in frequency domain
        freq=freq/(fftsize/2.)


        def countFFT():



            fftx =N.fft.fft(fftdata,fftsize)[0:fftsize]  #调用fft变换算法计算频域波形
            

            return abs(fftx)

        ffty = countFFT()


        self.plotWidget.canvas.ax.clear()
        self.plotWidget.canvas.ax.plot(freq,ffty,'-')
        self.plotWidget.canvas.draw()






if __name__ == "__main__":
    import sys    
    app = QApplication(sys.argv)

    plot = Plot_Widget()#data2plot,  varDict = totaldict)

    plot.show()
    sys.exit(app.exec_())     