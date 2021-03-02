import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
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
        t = np.arange(0, 35, 5)
        
        s1 = [58,63,69,70,72,68,60]
        s2 = [58,63,69,70,72,68,60]
        s3 = [-1,1,1,-1,1,-1,1]

        fig, axs = plt.subplots(3, sharex=True)
        obj = FigureCanvas(fig)
        fig.subplots_adjust(hspace=0.1)   # Remove horizontal space between axes

        # Plot each graph, and manually set the y tick values
        axs[0].scatter(t, s1)
        axs[0].plot(np.arange(0,31,1), [60 for _ in range(31)])
        axs[0].plot(np.arange(0,31,1), [110 for _ in range(31)])
        axs[0].set_yticks([40,70,100,130])
        axs[0].set_ylabel("HR", fontsize=10)
        axs[0].set_title("Realtime Details")

        axs[1].scatter(t, s2)
        axs[1].plot(np.arange(0,31,1), [60 for _ in range(31)])
        axs[1].plot(np.arange(0,31,1), [110 for _ in range(31)])
        axs[1].set_yticks([40,70,100,130])
        axs[1].set_ylabel("SDNN", fontsize=10)

        axs[2].scatter(t, s3)
        axs[2].plot(np.arange(0,31,1), [0 for _ in range(31)])
        axs[2].set_yticks([-1,0,1])
        axs[2].set_ylabel("RMSSD", fontsize=8)
        axs[2].set_xlabel("Time(s)", fontsize=10)

        plt.tight_layout()

        self.signal_layout1.addWidget(obj)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    ex = GUI() 
    ex.show()
    sys.exit(app.exec_())