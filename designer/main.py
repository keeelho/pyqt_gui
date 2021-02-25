# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logolbl = QtWidgets.QLabel(self.centralwidget)
        self.logolbl.setMinimumSize(QtCore.QSize(0, 50))
        self.logolbl.setMaximumSize(QtCore.QSize(16777215, 80))
        self.logolbl.setStyleSheet("background-color:rgb(0, 170, 255);")
        self.logolbl.setText("")
        self.logolbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logolbl.setObjectName("logolbl")
        self.verticalLayout.addWidget(self.logolbl)
        self.content_layout = QtWidgets.QWidget(self.centralwidget)
        self.content_layout.setObjectName("content_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_layout)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.right_layout = QtWidgets.QWidget(self.content_layout)
        self.right_layout.setObjectName("right_layout")
        self.face_frame = QtWidgets.QFrame(self.right_layout)
        self.face_frame.setGeometry(QtCore.QRect(20, 20, 640, 480))
        self.face_frame.setMinimumSize(QtCore.QSize(640, 480))
        self.face_frame.setMaximumSize(QtCore.QSize(640, 480))
        self.face_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(85, 0, 127);\n"
"    border-radius: 10;\n"
"}")
        self.face_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.face_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.face_frame.setObjectName("face_frame")
        self.groupBox_1 = QtWidgets.QGroupBox(self.right_layout)
        self.groupBox_1.setGeometry(QtCore.QRect(20, 520, 301, 48))
        self.groupBox_1.setObjectName("groupBox_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camera0 = QtWidgets.QCheckBox(self.groupBox_1)
        self.camera0.setObjectName("camera0")
        self.horizontalLayout_2.addWidget(self.camera0)
        self.video = QtWidgets.QCheckBox(self.groupBox_1)
        self.video.setObjectName("video")
        self.horizontalLayout_2.addWidget(self.video)
        self.camera1 = QtWidgets.QCheckBox(self.groupBox_1)
        self.camera1.setObjectName("camera1")
        self.horizontalLayout_2.addWidget(self.camera1)
        self.detail_graph1 = QtWidgets.QWidget(self.right_layout)
        self.detail_graph1.setGeometry(QtCore.QRect(690, 20, 501, 101))
        self.detail_graph1.setObjectName("detail_graph1")
        self.detail_graph2 = QtWidgets.QWidget(self.right_layout)
        self.detail_graph2.setGeometry(QtCore.QRect(690, 140, 501, 101))
        self.detail_graph2.setObjectName("detail_graph2")
        self.detail_graph3 = QtWidgets.QWidget(self.right_layout)
        self.detail_graph3.setGeometry(QtCore.QRect(690, 270, 501, 101))
        self.detail_graph3.setObjectName("detail_graph3")
        self.detail_graph4 = QtWidgets.QWidget(self.right_layout)
        self.detail_graph4.setGeometry(QtCore.QRect(690, 390, 501, 101))
        self.detail_graph4.setObjectName("detail_graph4")
        self.realtime_graph1 = QtWidgets.QWidget(self.right_layout)
        self.realtime_graph1.setGeometry(QtCore.QRect(380, 520, 391, 121))
        self.realtime_graph1.setObjectName("realtime_graph1")
        self.realtime_graph2 = QtWidgets.QWidget(self.right_layout)
        self.realtime_graph2.setGeometry(QtCore.QRect(800, 520, 391, 121))
        self.realtime_graph2.setObjectName("realtime_graph2")
        self.realtime_graph3 = QtWidgets.QWidget(self.right_layout)
        self.realtime_graph3.setGeometry(QtCore.QRect(380, 650, 391, 121))
        self.realtime_graph3.setObjectName("realtime_graph3")
        self.realtime_graph4 = QtWidgets.QWidget(self.right_layout)
        self.realtime_graph4.setGeometry(QtCore.QRect(800, 650, 391, 121))
        self.realtime_graph4.setObjectName("realtime_graph4")
        self.horizontalLayout.addWidget(self.right_layout)
        self.verticalLayout.addWidget(self.content_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_1.setTitle(_translate("MainWindow", "소스를 선택하세요."))
        self.camera0.setText(_translate("MainWindow", "내장카메라"))
        self.video.setText(_translate("MainWindow", "외장카메라"))
        self.camera1.setText(_translate("MainWindow", "비디오"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

