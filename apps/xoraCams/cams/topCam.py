
import os.path, time
import cv2, setproctitle
import multiprocessing as mp
# -- [ system ] --
from ...xoraCore.datatypes import *


RAM_DISK_ROOT: str = "/run/xor.ai"
IMAGE_SAVE_PATH: str = f"{RAM_DISK_ROOT}/cams/topcam"
PROC_NAME: str = "xor.ai/topcam"


class topCam(mp.Process):

   def __init__(self):
      super().__init__(target=self.__main__)
      # -- -- -- --
      if not os.path.exists(RAM_DISK_ROOT):
         raise FileNotFoundError(RAM_DISK_ROOT)
      # -- -- -- --
      rval: int = os.system(f"mkdir -p {IMAGE_SAVE_PATH}")
      # -- -- -- --
      self.cam: cv2.VideoCapture = cv2.VideoCapture()

   def run(self) -> None:
      pass

   def start(self) -> None:
      setproctitle.setproctitle(PROC_NAME)

   def __main__(self):
      def __tick() -> tickCode:
         pass
      # -- -- -- --
      while True:
         rval: tickCode = __tick()
         if rval == tickCode.OK:
            time.sleep(1.0)
         err, img = self.cam.read()
         print([err, img])
