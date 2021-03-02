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
        # details graphs
        t = np.arange(0, 35, 5)
        
        s1 = [58,63,69,70,72,68,60]
        s2 = [58,63,69,70,72,68,60]
        s3 = [-1,1,1,-1,1,-1,1]

        fig, axs = plt.subplots(3, sharex=True)
        obj1 = FigureCanvas(fig)
        fig.subplots_adjust(hspace=0)   # Remove horizontal space between axes

        # Plot each graph, and manually set the y tick values
        axs[0].scatter(t, s1, s=5, c='red')
        axs[0].plot(np.arange(0,31,1), [60 for _ in range(31)])
        axs[0].plot(np.arange(0,31,1), [110 for _ in range(31)])
        axs[0].set_yticks([])
        axs[0].set_ylabel("HR", fontsize=8)
        axs[0].set_title("Realtime Details", fontsize=10)

        axs[1].scatter(t, s2, s=5, c='magenta')
        axs[1].plot(np.arange(0,31,1), [60 for _ in range(31)])
        axs[1].plot(np.arange(0,31,1), [110 for _ in range(31)])
        axs[1].set_yticks([])
        axs[1].set_ylabel("SDNN", fontsize=8)

        axs[2].scatter(t, s3, s=5, c='green')
        axs[2].plot(np.arange(0,31,1), [0 for _ in range(31)])
        axs[2].set_yticks([])
        axs[2].set_ylabel("RMSSD", fontsize=8)
        axs[2].set_xlabel("Time(s)", fontsize=8)

        plt.tight_layout()

        self.detail_graph.addWidget(obj1)

        # # 3 realtime graphs
        ppg_time = np.arange(0,12,0.1)
        ppg = np.sin(ppg_time)

        fig2 = Figure()
        obj2 = FigureCanvas(fig2)

        ax2 = fig2.add_subplot(311)
        ax2.plot(ppg_time, ppg)
        ax2.set(xlabel='time', ylabel='PPG')

        ax3 = fig2.add_subplot(312)
        ax3.plot(ppg_time, ppg)
        ax3.set(xlabel='freqs', ylabel='FFT')

        ax4 = fig2.add_subplot(313)
        ax4.plot(ppg_time, ppg)
        ax4.set(xlabel='time', ylabel = 'Respiration')

        # fig2, axs2 = plt.subplots(3)
        # obj2 = FigureCanvas(fig2)
        # fig.subplots_adjust(hspace=0.3)

        # # PPG
        # axs2[0].plot(ppg_time, ppg)
        # axs2[0].set_title("PPG signal", fontsize=8)
        # axs2[0].set_xlabel("Time", fontsize=8)
        # axs2[0].set_ylabel("", fontsize=8)

        # # FFT
        # axs2[1].plot(ppg_time, ppg)
        # axs2[1].set_title("FFT", fontsize=8)
        # axs2[1].set_xlabel("freqs", fontsize=8)
        # axs2[1].set_ylabel("power", fontsize=8)

        # # Resp
        # axs2[2].plot(ppg_time, ppg)
        # axs2[2].set_title("Respiration rate", fontsize=8)
        # axs2[2].set_xlabel("Time", fontsize=8)
        # # axs2[2].set_ylabel("", fontsize=5)
        fig2.tight_layout()

        self.realtime_graph.addWidget(obj2)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    ex = GUI() 
    ex.show()
    sys.exit(app.exec_())