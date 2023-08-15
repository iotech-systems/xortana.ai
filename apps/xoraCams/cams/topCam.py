
"""
Available cameras
-----------------
0 : ov5647 [2592x1944] (/base/soc/i2c0mux/i2c@1/ov5647@36)
    Modes: 'SGBRG10_CSI2P' : 640x480 [58.92 fps - (16, 0)/2560x1920 crop]
                             1296x972 [43.25 fps - (0, 0)/2592x1944 crop]
                             1920x1080 [30.62 fps - (348, 434)/1928x1080 crop]
                             2592x1944 [15.63 fps - (0, 0)/2592x1944 crop]

"""

import os, sys, time
import threading

import cv2, setproctitle
import configparser as cp
import multiprocessing as mp
# -- [ system ] --
from apps.shared.core.datatypes import *


RAM_DISK_ROOT: str = "/run/xor.ai"
IMAGE_SAVE_PATH: str = f"{RAM_DISK_ROOT}/cams/topcam"
PROC_NAME: str = "xor.ai/topcam"
# TOP_CAM_INDEX: int = 0
# -- IMG INFO; 1920x1080 --
# IMG_WIDTH: int = 800
# IMG_HEIGHT: int = 800


class topCam(mp.Process):

   def __init__(self, sec: cp.SectionProxy):
      super(topCam, self).__init__(group=None, target=self._main, name=PROC_NAME)
      setproctitle.setproctitle(PROC_NAME)
      # -- -- -- --
      self.sec: cp.SectionProxy = sec
      if not os.path.exists(RAM_DISK_ROOT):
         raise FileNotFoundError(RAM_DISK_ROOT)
      print(f"[ topCam: PathFound: {RAM_DISK_ROOT} ]")
      rval: int = os.system(f"mkdir -p {IMAGE_SAVE_PATH}")
      # -- set top cam info --
      self.cam_idx: int = self.sec.get("TOP_CAM_INDEX")
      self.img_w: int = self.sec.getint("IMG_WIDTH")
      self.img_h: int = self.sec.getint("IMG_HEIGHT")
      self.img_freq: int = self.sec.getint("IMG_FREQ")
      self.cam: cv2.VideoCapture = cv2.VideoCapture(self.cam_idx)
      self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.img_w)
      self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.img_h)
      # -- -- -- --
      self.img_thread: threading.Thread = threading.Thread(target=self._img_thread)

   def _main(self):
      # -- main loop tick --
      def __tick() -> tickCode:
         # -- --
         return tickCode.OK
      # -- start proc threads --
      self.img_thread.start()
      # -- -- -- --
      while True:
         rval: tickCode = __tick()
         if rval == tickCode.OK:
            time.sleep(1.0)
         # -- -- -- --
         time.sleep(2.0)

   def _img_thread(self):
      def _tick() -> tickCode:
         err_code, img = self.cam.read()
         if err_code:
            fname: str = f"{IMAGE_SAVE_PATH}/topcam.png"
            cv2.imwrite(filename=fname, img=img)
            if os.path.exists(fname):
               print("img_taken_and_saved")
            return tickCode.OK
         else:
            print(["img_not_taken", err_code, self.cam])
            return tickCode.Error
      # -- -- -- --
      while True:
         sleep: float = 1000 / (self.img_freq * 1000)
         tick_code: tickCode = _tick()
         if tick_code == tickCode.OK:
            time.sleep(sleep)
         else:
            time.sleep(4.0)
