# -*- coding: UTF-8 -*-
"""
 # @Project     : lab1-asr
 # @File        : asrThread.py
 # #@Author     : mount_potato
 # @Date        : 2022/4/24 15:11
"""
import time

from PyQt5.QtCore import QThread, pyqtSignal
import os
import speech_recognition as sr
import socket
import difflib



def isNetConnected():
    try:
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


class ThreadASR(QThread):
    voiceSignal = pyqtSignal(str)
    finishSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.available_commands=['play music','open notepad','change']

    def getASR(self):
        try:
            r = sr.Recognizer()
            mic = sr.Microphone()
            # recognize
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            result=""
            if isNetConnected():
                result=r.recognize_google(audio)
                return None, result
            else:
                result=r.recognize_sphinx(audio)
                return None, result
        except sr.HTTPError:
                return "Network connection error",None
        except sr.WaitTimeoutError:
                return "Response Timeout",None
        except sr.RequestError:
                return "There's something wrong with sphinx",None
        except sr.UnknownValueError:
                return "Sphinx can't recognize this audio",None

    def run(self):
        while True:
            result=self.getASR()
            if result[0]:
                self.voiceSignal.emit(result[0])
                time.sleep(2)
                self.finishSignal.emit()
                continue
            print(result)
            self.voiceSignal.emit(result[1])
            time.sleep(2)
            self.finishSignal.emit()






