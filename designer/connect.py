import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import matplotlib as mpl
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm

form_class = uic.loadUiType("main.ui")[0]

class GUI(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setupUi(self)
        
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(False)
        self.btnPause.setEnabled(False)

        self.groupBox_2.setEnabled(False)

        # graph setting
        # figure1
        fig1 = Figure()
        obj1 = FigureCanvas(fig1)
        ax1 = fig1.add_subplot(111)
        ax1.plot(np.arange(0,60,1), [60 for _ in range(60)])
        ax1.plot(np.arange(0,60,1), [110 for _ in range(60)])
        x1 = [0,5,10,15,20,25,30,35,40,45,50,55]
        y1 = [58,63,69,70,72,68,60,59,70,68,65,60]
        ax1.scatter(x1,y1)
        fig1.patch.set_facecolor('white')
        ax1.patch.set_facecolor('white')
        ax1.set_xticks([0,10,20,30,40,50,60])
        ax1.set_yticks([40,70,100,130])
        # fig1.patch.set_alpha(0)
        # ax1.patch.set_alpha(0)
        # fig1.tight_layout()

        self.signal_layout1.addWidget(obj1)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    ex = GUI() 
    ex.show()
    sys.exit(app.exec_())