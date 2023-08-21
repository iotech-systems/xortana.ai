
import time
from picamera2 import picamera2
from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult


class skyCam(object):

   prefixIdx: {} = {}

   def __init__(self, act: str, args: str):
      self.act: str = act
      self.args: str = args
      self.cam: picamera2.Picamera2 = picamera2.Picamera2()

   def execute(self) -> execResult:
      if self.act == "take_img":

         self.__take_img()
      # -- -- -- --
      rval: execResult = execResult(0, "OK")
      return rval

   def __take_img(self, prefix: str):
      try:
         # -- -- -- --
         idx: int = 0
         if prefix in skyCam.prefixIdx.keys():
            idx = int(skyCam.prefixIdx[prefix])
         # -- -- -- --
         ffn: str = f"/opt/xortana.ai/tf/data/{prefix}_{idx}.jpg"
         SYS_TTS.say("I, will take an image in 3", 145)
         time.sleep(0.8)
         SYS_TTS.say("2", 150)
         time.sleep(0.8)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         self.cam.start_and_capture_file(ffn)
         skyCam.prefixIdx[prefix] = (idx + 1)
         # -- -- -- --
      except Exception as e:
         print(e)
