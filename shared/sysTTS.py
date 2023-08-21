
import pyttsx3


class sysTTS(object):

   def __init__(self):
     self.ttsEng = pyttsx3.init()

   def say(self, txt: str, rate: int):
      self.ttsEng.setProperty("rate", rate)
      self.ttsEng.say(txt)
      self.ttsEng.runAndWait()


# -- global --
SYS_TTS: sysTTS = sysTTS()
