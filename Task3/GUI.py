# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_9)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.harrisInput1 = QtWidgets.QLabel(self.frame_3)
        self.harrisInput1.setText("")
        self.harrisInput1.setPixmap(QtGui.QPixmap("screenshots/cat_rotate.jpeg"))
        self.harrisInput1.setScaledContents(True)
        self.harrisInput1.setObjectName("harrisInput1")
        self.verticalLayout_2.addWidget(self.harrisInput1)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.harrisOutput1 = QtWidgets.QLabel(self.frame_5)
        self.harrisOutput1.setText("")
        self.harrisOutput1.setPixmap(QtGui.QPixmap("screenshots/catHarris.png"))
        self.harrisOutput1.setScaledContents(True)
        self.harrisOutput1.setObjectName("harrisOutput1")
        self.verticalLayout.addWidget(self.harrisOutput1)
        self.gridLayout_8.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_5)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_9)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.harrisInput2 = QtWidgets.QLabel(self.frame_7)
        self.harrisInput2.setText("")
        self.harrisInput2.setPixmap(QtGui.QPixmap("screenshots/cat22.jpg"))
        self.harrisInput2.setScaledContents(True)
        self.harrisInput2.setObjectName("harrisInput2")
        self.verticalLayout_3.addWidget(self.harrisInput2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.harrisOutput2 = QtWidgets.QLabel(self.frame_8)
        self.harrisOutput2.setText("")
        self.harrisOutput2.setPixmap(QtGui.QPixmap("screenshots/reult2.jpg"))
        self.harrisOutput2.setScaledContents(True)
        self.harrisOutput2.setObjectName("harrisOutput2")
        self.verticalLayout_4.addWidget(self.harrisOutput2)
        self.gridLayout_10.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Ma = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ma.setFont(font)
        self.Ma.setAlignment(QtCore.Qt.AlignCenter)
        self.Ma.setObjectName("Ma")
        self.verticalLayout_5.addWidget(self.Ma)
        self.MatchingImage = QtWidgets.QLabel(self.frame_4)
        self.MatchingImage.setText("")
        self.MatchingImage.setPixmap(QtGui.QPixmap("screenshots/match.PNG"))
        self.MatchingImage.setScaledContents(True)
        self.MatchingImage.setAlignment(QtCore.Qt.AlignCenter)
        self.MatchingImage.setObjectName("MatchingImage")
        self.verticalLayout_5.addWidget(self.MatchingImage)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Harris Input 1"))
        self.label_2.setText(_translate("MainWindow", "Harris Output 1"))
        self.label_5.setText(_translate("MainWindow", "Harris Input 2"))
        self.label_7.setText(_translate("MainWindow", "Harris Output 2"))
        self.Ma.setText(_translate("MainWindow", "Matching Image with the template"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
