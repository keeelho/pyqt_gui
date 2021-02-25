from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

from main import Ui_MainWindow

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())