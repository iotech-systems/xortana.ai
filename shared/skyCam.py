import time

from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult

class skyCam(object):

   def __init__(self, act: str, args: str):
      self.act: str = act
      self.args: str = args

   def execute(self) -> execResult:
      if self.act == "take_img":
         self.__take_img()
      # -- -- -- --
      rval: execResult = execResult(0, "OK")
      return rval

   def __take_img(self):
      SYS_TTS.say("I will take an image in 3", 150)
      time.sleep(0.8)
      SYS_TTS.say("2", 150)
      time.sleep(0.8)
      SYS_TTS.say("1", 150)
