# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from asrThread import ERROR,UNCLEAR,MUSIC,FILE

class ASR_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 580)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # siri gif
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(70, 30, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("../icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        # how can i help
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 175, 200, 42))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        # You can
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        # Enjoy music
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 201, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        # Open file
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 330, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def responseToVoiceThread(self,CODE,voiceText):
        """
        the change of view when a voice command is raised
        """
        _translate = QtCore.QCoreApplication.translate

        if CODE==ERROR:
            self.label.setText(_translate("MainWindow", voiceText))
            self.label_2.hide()
        elif CODE==UNCLEAR:
            self.label.setText(_translate("MainWindow", voiceText))
            self.label_2.setText(_translate("MainWindow", "Sorry I don't get it..."))
        elif CODE==MUSIC:
            self.label.setText(_translate("MainWindow", voiceText))
            self.label_2.setText(_translate("MainWindow", "Opening the music file..."))
        elif CODE==FILE:
            self.label.setText(_translate("MainWindow", voiceText))
            self.label_2.setText(_translate("MainWindow", "Opening the txt file..."))
        else: #CODE==VIDEO
            self.label.setText(_translate("MainWindow", voiceText))
            self.label_2.setText(_translate("MainWindow", "Opening the video file..."))


        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()


    def returnToMainPage(self):
        """
        the change of view when command execution is finished
        """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.voiceFig.show()
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open file\""))
        self.label_5.setText(_translate("MainWindow", "3. Watch an video by saying \"Play Video\""))

