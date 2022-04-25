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


ERROR=-1
UNCLEAR=-2
MUSIC=0
FILE=1
VIDEO=2

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
    voiceSignal = pyqtSignal(int,str)
    finishSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.available_commands=['play music','open file',"play video"]

    def getASR(self):

        try:
            r = sr.Recognizer()
            mic = sr.Microphone()

            if not isinstance(r, sr.Recognizer):
                raise TypeError("`recognizer` must be `Recognizer` instance")
            if not isinstance(mic, sr.Microphone):
                raise TypeError("`microphone` must be `Microphone` instance")
            # recognize
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            if isNetConnected():
                result=r.recognize_google(audio)
                if result=="":
                    raise sr.UnknownValueError
                return None, result
            else:
                result=r.recognize_sphinx(audio)
                if result=="":
                    raise sr.UnknownValueError
                return None, result
        except sr.HTTPError:
            return "Network connection error, returning in 2s...",None
        except sr.WaitTimeoutError:
            return "Response Timeout,returning in 2s...",None
        except sr.RequestError or TypeError:
            return "There's something wrong with sphinx,returning in 2s...",None
        except sr.UnknownValueError:
            return "Sphinx can't recognize this audio,returning in 2s...",None

    def run(self):
        while True:
            result=self.getASR()
            if result[0]:
                # error message inform
                self.voiceSignal.emit(ERROR,result[0])
                time.sleep(2)
                self.finishSignal.emit()
                continue
            else:
                # sending sr result
                # self.voiceSignal.emit(result[1])
                command_rate_list=[string_similar(result[1],i) for i in self.available_commands]
                command_max_rate=max(command_rate_list)
                command_idx=-1 if command_max_rate<0.4 else command_rate_list.index(command_max_rate)
                if command_idx ==MUSIC:
                    self.voiceSignal.emit(MUSIC,result[1])
                    os.system("open resources/f1lcapae.wav")
                elif command_idx == FILE:
                    self.voiceSignal.emit(FILE, result[1])
                    os.system("open resources/text.txt")
                elif command_idx == VIDEO:
                    self.voiceSignal.emit(VIDEO, result[1])
                    os.system("open resources/video.mp4")
                else: #command_idx=-1
                    self.voiceSignal.emit(UNCLEAR, result[1])
                time.sleep(2)
                self.finishSignal.emit()









