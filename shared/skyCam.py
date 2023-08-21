
import os.path, time
try:
   from picamera2.picamera2 import Picamera2 as PiCam2
except ModuleNotFoundError:
   # this mics code rpi calls running on ubuntu
   from shared.stubs.picam2 import picam2stub as PiCam2
# -- keep loading --
from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult


class skyCam(object):

   TF_DATA_FOLDER: str = "/opt/xortana.ai/tf/data"
   prefixIdx: {} = {}
   CAM: PiCam2 = None

   def __init__(self, act: str, args: str):
      self.act: str = act
      self.args: str = args
      if skyCam.CAM is None:
         skyCam.CAM = PiCam2()

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
         ffn: str = f"{skyCam.TF_DATA_FOLDER}/{prefix}_{idx:03}.jpg"
         SYS_TTS.say("I, will take an image in 3", 150)
         time.sleep(0.8)
         SYS_TTS.say("2", 150)
         time.sleep(0.8)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         skyCam.CAM.start_and_capture_file(ffn, show_preview=False)
         skyCam.prefixIdx[prefix] = (idx + 1)
         if os.path.exists(ffn):
            SYS_TTS.say("image has been taken", 150)
         # -- -- -- --
      except Exception as e:
         print(e)
