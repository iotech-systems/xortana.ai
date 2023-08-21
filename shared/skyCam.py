
import os.path, time

import picamera2.picamera2

try:
   from picamera2.picamera2 import Picamera2 as PiCam2
   from picamera2.picamera2 import NullPreview
except ModuleNotFoundError:
   # this mics code rpi calls running on ubuntu
   from shared.stubs.picam2 import picam2stub as PiCam2
# -- keep loading --
from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult


class skyCam(object):

   TF_DATA_FOLDER: str = "/opt/xortana.ai/tf/data"
   prefixIdx: {} = {}

   def __init__(self, act: str, args: str):
      self.act: str = act
      self.args: str = args
      self.cam: PiCam2 = PiCam2()

   def execute(self) -> execResult:
      if self.act == "take_img":
         self.__take_img(self.args)
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
         if not os.path.exists(skyCam.TF_DATA_FOLDER):
            raise FileNotFoundError(skyCam.TF_DATA_FOLDER)
         # -- -- -- --
         ffn: str = f"{skyCam.TF_DATA_FOLDER}/{prefix}_{idx}.jpg"
         SYS_TTS.say("I, will take an image in 3", 145)
         time.sleep(0.8)
         SYS_TTS.say("2", 150)
         time.sleep(0.8)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         self.cam.start_and_capture_file(ffn, show_preview=False)
         skyCam.prefixIdx[prefix] = (idx + 1)
         # -- -- -- --
      except Exception as e:
         print(e)
