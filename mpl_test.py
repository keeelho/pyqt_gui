from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import sys

import matplotlib as mpl
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm


class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(350, 60, 1200, 870)
        self.setStyleSheet("background-color: white;")

        result = np.loadtxt('result.csv', delimiter=',')
        print(result.shape)

        # frame1
        faceframe = QtWidgets.QFrame()
        faceframe.setStyleSheet('background-color: rgb(0,0,0);')

        # figure1
        fig1 = Figure()
        obj1 = FigureCanvas(fig1)
        ax1 = fig1.add_subplot(111)
        x1 = result[0,:]
        y1 = result[1,:]
        ax1.plot(x1, y1)
        fig1.tight_layout()

        # figure2
        fig2 = Figure()
        obj2 = FigureCanvas(fig2)
        ax2 = fig2.add_subplot(111)
        x2 = np.linspace(0, 4*np.pi, 15)
        y2 = np.sin(2 * (x2 - 0.1))
        ax2.plot(x2, y2)
        
        # figure3
        fig3 = Figure()
        obj3 = FigureCanvas(fig3)
        ax3 = fig3.add_subplot(111)
        x3 = np.linspace(0, 4*np.pi, 15)
        y3 = np.sin(2 * (x3 - 0.1))
        ax3.plot(x3, y3)
        
        # figure4
        fig4 = Figure()
        obj4 = FigureCanvas(fig4)
        ax4 = fig4.add_subplot(111)
        x4 = np.linspace(0, 4*np.pi, 15)
        y4 = np.sin(2 * (x4 - 0.1))
        ax4.plot(x4, y4)

        #
        right_inner = QtWidgets.QVBoxLayout()
        right_inner.addWidget(obj1)
        right_inner.addWidget(obj2)
        right_inner.addWidget(obj3)
        right_inner.addWidget(obj4)
        
        # content
        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(faceframe)
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addLayout(right_inner)
        
        # layout
        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(left_layout)
        layout.addLayout(right_layout)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())