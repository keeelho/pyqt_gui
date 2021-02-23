from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(350, 60, 1200, 870)
        self.setStyleSheet("background-color: white;")

        #
        title_line = QtWidgets.QLineEdit()

        #
        left_content1 = QtWidgets.QLineEdit()
        left_content2 = QtWidgets.QLineEdit()
        left_content3 = QtWidgets.QLineEdit()
        right_content1 = QtWidgets.QLineEdit()
        right_content2 = QtWidgets.QLineEdit()
        right_content3 = QtWidgets.QLineEdit()
        right_content4 = QtWidgets.QLineEdit()

        #
        leftinnerlayout = QtWidgets.QVBoxLayout()
        leftinnerlayout.addWidget(left_content1)
        leftinnerlayout.addWidget(left_content2)
        leftinnerlayout.addWidget(left_content3)
        rightinnerlayout = QtWidgets.QVBoxLayout()
        rightinnerlayout.addWidget(right_content1)
        rightinnerlayout.addWidget(right_content2)
        rightinnerlayout.addWidget(right_content3)
        rightinnerlayout.addWidget(right_content4)
        
        #
        upperLayout = QtWidgets.QHBoxLayout()
        upperLayout.addWidget(title_line)

        downLayout = QtWidgets.QHBoxLayout()
        downLayout.addLayout(leftinnerlayout)
        downLayout.addLayout(rightinnerlayout)
        
        #
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(upperLayout)
        layout.addStretch(1)
        layout.addLayout(downLayout)
        layout.addStretch(9)
        
        #
        self.setLayout(layout)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(Qt.red, 10, Qt.SolidLine))
        
        painter.drawRect(750, 200, 300, 50)

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())