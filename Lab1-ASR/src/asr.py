from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import ASR_MainWindow
import sys

from asrThread import ThreadASR


import speech_recognition as sr

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = ASR_MainWindow()
        self.ui.setupUi(self)
        self.asrThread=ThreadASR()
        self.asrThread.voiceSignal.connect(self.responseVoiceSignal)
        self.asrThread.finishSignal.connect(self.responseFinishSignal)
        self.asrThread.start()

    def responseVoiceSignal(self,CODE,context):
        self.ui.responseToVoiceThread(CODE,context)

    def responseFinishSignal(self):
        self.ui.returnToMainPage()



app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

