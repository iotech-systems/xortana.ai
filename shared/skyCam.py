
import os.path, time
from PIL import Image
try:
   from picamera2.picamera2 import Picamera2 as PiCam2
except ModuleNotFoundError:
   # this mics code rpi calls running on ubuntu
   from shared.stubs.picam2 import picam2stub as PiCam2
# -- keep loading --
from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult


class skyCam(object):

   prefixIdx: {} = {}
   CAM: PiCam2 = None
   TF_IMGS_FOLDER: str = "/opt/xortana.ai/tf/imgs"
   TF_THUMS_FOLDER: str = "/opt/xortana.ai/tf/thums"

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
         if not os.path.exists(skyCam.TF_IMGS_FOLDER):
            raise FileNotFoundError(skyCam.TF_IMGS_FOLDER)
         # -- -- -- --
         img_name: str = f"{prefix}_{idx:03}.jpg"
         ffn: str = f"{skyCam.TF_IMGS_FOLDER}/{img_name}"
         SYS_TTS.say("New image in 3", 150)
         time.sleep(0.6)
         SYS_TTS.say("2", 150)
         time.sleep(0.6)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         skyCam.CAM.start_and_capture_file(ffn, show_preview=False)
         skyCam.prefixIdx[prefix] = (idx + 1)
         if os.path.exists(ffn):
            img: Image = Image.open(ffn)
            img.thumbnail((324, 243))
            # thum_path: str = f"{skyCam.TF_THUMS_FOLDER}/thm_{img_name}"
            img.save(f"{skyCam.TF_THUMS_FOLDER}/thm_{img_name}")
            SYS_TTS.say("Image has been taken", 150)
         # -- -- -- --
      except Exception as e:
         print(e)
