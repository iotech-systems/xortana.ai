
import os, sys, time
import cv2, setproctitle
import multiprocessing as mp
# -- [ system ] --
from apps.shared.core.datatypes import *


RAM_DISK_ROOT: str = "/run/xor.ai"
IMAGE_SAVE_PATH: str = f"{RAM_DISK_ROOT}/cams/topcam"
PROC_NAME: str = "xor.ai/topcam"
TOP_CAM_INDEX: int = 0
# -- IMG INFO --
IMG_WIDTH: int = 800
IMG_HEIGHT: int = 600


class topCam(mp.Process):

   def __init__(self):
      super(topCam, self).__init__(group=None, target=self.__main__, name=PROC_NAME)
      setproctitle.setproctitle(PROC_NAME)
      # -- -- -- --
      if not os.path.exists(RAM_DISK_ROOT):
         raise FileNotFoundError(RAM_DISK_ROOT)
      print(f"[ topCam: PathFound: {RAM_DISK_ROOT} ]")
      rval: int = os.system(f"mkdir -p {IMAGE_SAVE_PATH}")
      # -- set top cam info --
      self.cam: cv2.VideoCapture = cv2.VideoCapture(TOP_CAM_INDEX)
      self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_WIDTH)
      self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_HEIGHT)

   def __main__(self):
      # -- main loop tick --
      def __tick() -> tickCode:
         err_code, img = self.cam.read()
         if err_code:
            fname: str = f"{IMAGE_SAVE_PATH}/topcam.png"
            cv2.imwrite(filename=fname, img=img)
            if os.path.exists(fname):
               print("img_taken_and_saved")
         else:
            print("img_not_taken")
         # -- --
         return tickCode.OK
      # -- -- -- --
      while True:
         rval: tickCode = __tick()
         if rval == tickCode.OK:
            time.sleep(1.0)
         # -- -- -- --
         time.sleep(2.0)
