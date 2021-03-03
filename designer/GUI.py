import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm

form_class = uic.loadUiType("main.ui")[0]

class GUI(QtWidgets.QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setupUi(self)

        self.plot_graph()

        # Playbutton
        self.btnStart.setEnabled(False)
        self.btnStart.clicked.connect(self.start)
        # Stopbutton
        self.btnStop.setEnabled(False)
        self.btnStop.clicked.connect(self.stop)
        # Openbutton
        self.btnOpen.setEnabled(False)
        self.btnOpen.clicked.connect(self.openFileDialog)
        # Timer
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        # ComboBox1
        self.cbbInput.addItem("Select Your Input")
        self.cbbInput.addItem("Webcam : 0")
        self.cbbInput.addItem("Webcam : 1")
        self.cbbInput.addItem("Video")
        self.cbbInput.activated.connect(self.selectInput)
        # ComboBox2
        self.cbbInput2.addItem("Select Mode")
        self.cbbInput2.addItem("Mode : Manual")
        self.cbbInput2.addItem("Mode : Auto")

    def update(self):
        if self.cbbInput.currentIndex() == 1:
            pass
            # self.frame, self.startX, self.startY, self.endX, self.endY, self.frame_time = self.input.get_frame()
            # if self.startX > 0:
            #     self.process.frame_in = self.frame
            #     self.process.startX = self.startX
            #     self.process.startY = self.startY
            #     self.process.endX = self.endX
            #     self.process.endY = self.endY
            #     self.process.frame_time = self.frame_time
            #     self.process.run()
            # self.plotter()

        elif self.cbbInput.currentIndex() == 2:
            pass
            # self.frame, self.startX, self.startY, self.endX, self.endY, self.frame_time = self.input.get_frame()
            # if self.startX > 0:
            #     self.process.frame_in = self.frame
            #     self.process.startX = self.startX
            #     self.process.startY = self.startY
            #     self.process.endX = self.endX
            #     self.process.endY = self.endY
            #     self.process.frame_time = self.frame_time
            #     self.process.run()
        elif self.cbbInput.currentIndex() == 3:
            pass

    def selectInput(self):
        if self.cbbInput.currentIndex() == 1:
            print("camera0 is selected")
            # self.reset()
            # # time widget should be reset
            self.cbbInput2.setEnabled(False)
            self.btnStart.setEnabled(True)
            self.input = Webcam()
            self.input.cam_id = 0
            self.process = Process_webcam()
            # self.resBtn.setEnabled(False)
        if self.cbbInput.currentIndex() == 2:
            print("camera1 is selected")
            # self.reset()
            # # time widget should be reset
            self.cbbInput2.setEnabled(False)
            self.btnStart.setEnabled(True)
            self.input = Webcam()
            self.input.cam_id = 1
            self.process = Process_webcam()
            # self.resBtn.setEnabled(False)
        if self.cbbInput.currentIndex() == 3:
            print("video is selected")
            # self.reset()
            # # time widget should be reset
            self.btnStart.setEnabled(False)
            self.cbbInput2.setEnabled(True)
            self.cbbInput2.activated.connect(self.videoInput)
        else:
            self.reset()

    def reset(self):
        pass

    def videoInput(self):
        if self.cbbInput2.currentIndex() == 0:
            print("Please Choose your video detect type")
            self.btnOpen.setEnabled(False)
        elif self.cbbInput2.currentIndex() == 1:
            print("Auto detect is selected")
            self.btnOpen.setEnabled(True)
            self.btnStart.setEnabled(True)
        elif self.cbbInput2.currentIndex() == 2:
            print("Manual detect is selected")
            self.btnOpen.setEnabled(True)
            self.btnStart.setEnabled(True)

    def start(self):
        self.reset()
        self.input.start()
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(True)
        self.timer.start()

    def stop(self):
        self.input.stop()
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(False)
        self.cbbInput.setEnabled(True)
        self.resBtn.setEnabled(True)
        self.timer.stop()
        self.lblDisplay.clear()

    def openFileDialog(self):
        self.dirname, _x = QtGui.QFileDialog.getOpenFileName(self)
        print(self.dirname)

    def closeEvent(self, event):
        self.timer.stop()
        super(QtWidgets.QMainWindow, self).closeEvent(event)
    
    def plotter(self):
        pass

    def plot_graph(self):
        # graph setting
        # details graphs
        t = np.arange(0, 66, 5)
        s1 = [58,63,69,70,72,68,60,58,63,69,70,72,68,60]
        s2 = [58,63,69,70,72,68,60,58,63,69,70,72,68,60]
        s3 = [-1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1]

        fig, axs = plt.subplots(3, sharex=True)
        obj1 = FigureCanvas(fig)
        fig.subplots_adjust(hspace=0)   # Remove horizontal space between axes

        # Plot each graph, and manually set the y tick values
        axs[0].scatter(t, s1, s=5, c='red')
        axs[0].plot(np.arange(0,61,1), [60 for _ in range(61)], color='green')
        axs[0].plot(np.arange(0,61,1), [110 for _ in range(61)], color='green')
        axs[0].set_yticks([])
        axs[0].set_ylabel("HR", fontsize=8)
        axs[0].set_title("Realtime Details", fontsize=10)
        axs[0].set(ylim=[40,130])

        axs[1].scatter(t, s2, s=5, c='magenta')
        axs[1].plot(np.arange(0,61,1), [60 for _ in range(61)], color='green')
        axs[1].plot(np.arange(0,61,1), [110 for _ in range(61)], color='green')
        axs[1].set_yticks([])
        axs[1].set_ylabel("SDNN", fontsize=8)
        axs[1].set(ylim=[40,130])

        # axs[2].scatter(t, s3, s=5, c='green')
        axs[2].bar(t, s3, align='edge', alpha=0.5, color='green')
        axs[2].plot(np.arange(0,61,1), [0 for _ in range(61)], color='green')
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
        ax2.set_title('Realtime graphs', fontsize=10)
        ax2.set_yticks([])
        ax2.set_xlabel('Time(s)', fontsize=8)
        ax2.set_ylabel('PPG', fontsize=9)

        ax3 = fig2.add_subplot(312)
        ax3.plot(ppg_time, ppg)
        ax3.set_yticks([])
        ax3.set_xlabel('Freqs(hz)', fontsize=8)
        ax3.set_ylabel('FFT', fontsize=9)

        ax4 = fig2.add_subplot(313)
        ax4.plot(ppg_time, ppg)
        ax4.set_yticks([])
        ax4.set_xlabel('Time(s)', fontsize=8)
        ax4.set_ylabel('Respiration', fontsize=9)

        fig2.tight_layout()

        self.realtime_graph.addWidget(obj2)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    ex = GUI() 
    ex.show()
    sys.exit(app.exec_())