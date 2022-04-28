# HCI-Assignment-2

- Course: Human Computer Interaction
- Student: Chen Kaixin
- ID: 1951724
- Tutor: Shen Ying

## Installation and Run

Locate to the homework directory, and use conda to install the dependencies through the requirement file:

```bash
conda create -n asr python==3.7
conda activate asr
pip install -r requirements.txt
```

After activating the environment, enter:

```bash
python src/asr.py
```

 **It’s recommended to turn on the VPN, otherwise it may stuck.**

## Project Structure

```c
.
├── doc
│   ├── HCI-Assignment-2\ a888c59bfa4a4f958968d553ab15d959
│   │   ├── Untitled\ 1.png
│   │   └── Untitled.png
│   └── HCI-Assignment-2\ a888c59bfa4a4f958968d553ab15d959.md
├── icon
│   ├── phone.png
│   ├── play.gif
│   └── voice.gif
├── requirements.txt
├── resources
│   ├── f1lcapae.wav
│   ├── text.txt
│   └── video.mp4
└── src
    ├── __pycache__
    │   ├── asrInterface.cpython-37.pyc
    │   └── asrThread.cpython-37.pyc
    ├── asr.py
    ├── asrInterface.py
    └── asrThread.py

```

## Main Function and Source Code

In this automatic speech recognition demo, you can:

- Enjoy music by **saying “Play Music”**
- Take some notes by **saying “Open File”**
- Watch an video by **saying “Play Video”**

By executing the voice command, the interface will show specific response.

### Communication

The program uses QThread to implement the  function logic. The logic thread will emit two `pyqtSignal` when the thread requires ui changes. In the main window class (QtWidgets.QMainWindow), the thread and the ui class object is initialized. After receiving the signals from the thread, the main window will demands ui changes on ui.

```python
# in asrInterface.py

class myWindow(QtWidgets.QMainWindow):

	def __init__(self):
			# init the ui
      self.ui = ASR_MainWindow()
      self.ui.setupUi(self)

			# init the logic thread
      self.asrThread=ThreadASR()
			# connect the thread signal with the response function
      self.asrThread.voiceSignal.connect(self.responseVoiceSignal)
      self.asrThread.finishSignal.connect(self.responseFinishSignal)
      self.asrThread.start()

	def responseVoiceSignal(self,CODE,context):
			# demanding the changes of ui
      self.ui.responseToVoiceThread(CODE,context)

  def responseFinishSignal(self):
			# demanding the changes of ui
      self.ui.returnToMainPage()

# in asrThread.py
class ThreadASR(QThread):
	  voiceSignal = pyqtSignal(int,str)
    finishSignal = pyqtSignal()
		
		...

		def run(self):
				...
				# when the thread requires ui changes 

				# for command signal
				self.voiceSignal.emit(MUSIC,"xxx") 

				# for finish signal
				self.finishSignal.emit()

# in asrInterface.py:

class ASR_MainWindow(object):
		...
		def responseToVoiceThread(self,CODE,voiceText):
			  # ui changes to voiceSignal

		def returnToMainPage(self):
				# ui changes to finishSignal
```

### Recognition

The demo uses pocketsphinx to recognize the audio.

```python

def getASR(self):
	...
	try:
	     r = sr.Recognizer()
	     mic = sr.Microphone()
	
	if not isinstance(r, sr.Recognizer):
	     raise TypeError("`recognizer` must be `Recognizer` instance")
	if not isinstance(mic, sr.Microphone):
	     raise TypeError("`microphone` must be `Microphone` instance")
	
	with mic as source:
	     r.adjust_for_ambient_noise(source)
	     audio = r.listen(source)

	 ...
```

### Accuracy improvement

Since the original function `recognize_sphinx` has very low performances on voice recognition, we could use other api like google to improve the accuracy. **It’s recommended to turn on the VPN since the google api is unstable.**

The demo will check for net connection before applying the google api. If it’s offline, the original function will be used.

```python
# in asrThread.py

def isNetConnected():
    try:
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False

class ThreadASR(QThread):
		...
		def getASR(self):
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
```

## Command Logic

The demo will check for the most similar command for the speech recognition result using `difflib` . If the similarity is high enough, the command will be called using `os.system` .


```python
command_rate_list=[string_similar(result[1],i) for i in self.available_commands]
command_max_rate=max(command_rate_list)
command_idx=-1 if command_max_rate<0.4 else command_rate_list.index(command_max_rate)
if command_idx ==MUSIC:
   self.voiceSignal.emit(MUSIC,result[1])
   os.system("open resources/f1lcapae.wav")
...
```

## GUI

based on the original demo, some modification is applied.

- error handling

![Untitled](HCI-Assignment-2%20a888c59bfa4a4f958968d553ab15d959/Untitled.png)

- recognize result display and corresponding response

![Untitled](HCI-Assignment-2%20a888c59bfa4a4f958968d553ab15d959/Untitled%201.png)