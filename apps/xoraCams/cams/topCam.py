
import os, sys, time
import cv2, setproctitle
import multiprocessing as mp
# sys.path.insert(0, "..")
# -- [ system ] --
from apps.shared.core.datatypes import *


RAM_DISK_ROOT: str = "/run/xor.ai"
IMAGE_SAVE_PATH: str = f"{RAM_DISK_ROOT}/cams/topcam"
PROC_NAME: str = "xor.ai/topcam"
TOP_CAM_INDEX: int = 0


class topCam(mp.Process):

   def __init__(self):
      super(topCam, self).__init__(target=self.__main__)
      # -- -- -- --
      if not os.path.exists(RAM_DISK_ROOT):
         raise FileNotFoundError(RAM_DISK_ROOT)
      # -- -- -- --
      rval: int = os.system(f"mkdir -p {IMAGE_SAVE_PATH}")
      # -- -- -- --
      self.cam: cv2.VideoCapture = cv2.VideoCapture(TOP_CAM_INDEX)

   def start(self) -> None:
      setproctitle.setproctitle(PROC_NAME)
      super().start()

   def __main__(self):
      # -- main loop tick --
      def __tick() -> tickCode:
         err_code, img = self.cam.read()
         if err_code:
            pass
         else:
            pass
         # -- --
         return tickCode.OK
      # -- -- -- --
      while True:
         rval: tickCode = __tick()
         if rval == tickCode.OK:
            time.sleep(1.0)
         # -- -- -- --
         time.sleep(2.0)
