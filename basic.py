from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import sys

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(350, 60, 1200, 870)
        self.setStyleSheet("background-color: white;")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())