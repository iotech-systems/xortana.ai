
import pyttsx3

class sysTTS(object):

   def __init__(self):
     self.ttsEng = pyttsx3.init()

   def say(self, txt: str, rate: int):
      try:
         self.ttsEng.setProperty("rate", rate)
         self.ttsEng.say(txt)
         self.ttsEng.runAndWait()
      except Exception as e:
         print(e)


# -- [ global ] --
SYS_TTS: sysTTS = sysTTS()
# pitch = float(SYS_TTS.ttsEng.getProperty("pitch"))
# SYS_TTS.ttsEng.setProperty("pitch", (pitch - 0.5))
