
"""
xora@xortana:~ $ libcamera-still --list-cameras
Available cameras
-----------------
   0 : ov5647 [2592x1944] (/base/soc/i2c0mux/i2c@1/ov5647@36)
       Modes: 'SGBRG10_CSI2P' : 640x480 [30.00 fps - (0, 0)/0x0 crop]
                                1296x972 [30.00 fps - (0, 0)/0x0 crop]
                                1920x1080 [30.00 fps - (0, 0)/0x0 crop]
                                2592x1944 [30.00 fps - (0, 0)/0x0 crop]
"""

import threading
import os.path, time, queue
from PIL import Image
try:
   from picamera2.picamera2 import Picamera2 as PiCam2
except ModuleNotFoundError:
   # this mics code rpi calls running on ubuntu
   from shared.stubs.picam2 import picam2stub as PiCam2
# -- keep loading --
from shared.sysTTS import SYS_TTS
from shared.datatypes import execResult
from shared.sysSnd import sysSnd


MAX_WIDTH: int = 2592
MAX_HEIGHT: int = 1944
SIZE_DIV: int = 3


IMG_SIZE: () = (MAX_WIDTH, MAX_HEIGHT)
THUM_SIZE: () = (int(MAX_WIDTH / SIZE_DIV), int(MAX_HEIGHT / SIZE_DIV))


class skyCam(object):

   CAM_THREAD_TICK_MS: int = 0.480
   prefixIdx: {} = {}
   CAM: PiCam2 = None
   RAM_DISK: str = "/run/xora.ai"
   TF_IMGS_FOLDER: str = "/opt/xortana.ai/tf/imgs"
   TF_THUMS_FOLDER: str = "/opt/xortana.ai/tf/thums"
   CAM_LOCK: threading.Lock = threading.Lock()
   __inst = None

   @staticmethod
   def Instance():
      # -- -- -- --
      if not os.path.exists(skyCam.RAM_DISK):
         os.makedirs(skyCam.RAM_DISK)
      # -- -- -- --
      if skyCam.__inst is None:
         skyCam.__inst = skyCam()
      # -- -- -- --
      return skyCam.__inst

   def __init__(self):
      if skyCam.CAM is None:
         skyCam.CAM = PiCam2()
         conf = skyCam.CAM.create_still_configuration(main={"size": IMG_SIZE})
         skyCam.CAM.configure(conf)
         skyCam.CAM.start()
      # -- -- -- --
      self.img_cnt: int = 0
      self.cam_thread: threading.Thread = threading.Thread(target=self.__cam_thread)
      self.cmd_thread: threading.Thread = threading.Thread(target=self.__cmd_thread)

   def start_cam_threads(self):
      self.cam_thread.start()
      self.cmd_thread.start()

   def web_take_img(self, prefix: str) -> [None, execResult]:
      try:
         # -- -- -- --
         idx: int = 0
         if prefix in skyCam.prefixIdx.keys():
            idx = int(skyCam.prefixIdx[prefix])
         # -- -- -- --
         if not os.path.exists(skyCam.TF_IMGS_FOLDER):
            os.makedirs(skyCam.TF_IMGS_FOLDER)
         if not os.path.exists(skyCam.TF_IMGS_FOLDER):
            raise FileNotFoundError(skyCam.TF_IMGS_FOLDER)
         # -- -- -- --
         img_name: str = f"{prefix}_{idx:03}.jpg"
         ffn: str = f"{skyCam.TF_IMGS_FOLDER}/{img_name}"
         # SYS_TTS.say("New image in 3", 150)
         # time.sleep(0.2)
         # SYS_TTS.say("2", 150)
         # time.sleep(0.2)
         # SYS_TTS.say("1", 150)
         sysSnd.play_tone("hz560", 2)
         # -- -- -- --
         self.__take_img(ffn)
         skyCam.prefixIdx[prefix] = (idx + 1)
         if os.path.exists(ffn):
            img: Image = Image.open(ffn)
            img.thumbnail(THUM_SIZE)
            img.save(f"{skyCam.TF_THUMS_FOLDER}/thm_{img_name}")
            # SYS_TTS.say("Image has been taken", 150)
            sysSnd.play_tone("hz660")
         # -- -- -- --
         rval: execResult = execResult(0, "OK")
         return rval
      except Exception as e:
         print(e)
         return None
      finally:
         try:
            if skyCam.CAM_LOCK.locked():
               skyCam.CAM_LOCK.release()
         except Exception as e:
            print(e)

   def __cmd_thread(self):
      # -- -- -- --
      cmd_file: str = f"{skyCam.RAM_DISK}/skycam/cmd.txt"
      def __th_tick() -> int:
         if not os.path.exists(cmd_file):
            return 1
         with open(cmd_file, "r") as f:
            cmd_body = f.read().strip()
         os.unlink(cmd_file)
         if cmd_body.startswith("web_take_img:"):
            _, prefix = cmd_body.split(":")
            self.web_take_img(prefix)
         else:
            pass
      # -- -- -- --
      while True:
         rval: int = __th_tick()
         time.sleep(1.0)

   def __cam_thread(self):
      # -- -- -- --
      rnd_q: queue.SimpleQueue = queue.SimpleQueue()
      [rnd_q.put(i) for i in range(0, 8)]
      sky_cam_fld: str = f"{skyCam.RAM_DISK}/skycam"
      try:
         if not os.path.exists(sky_cam_fld):
            os.system(f"cd {skyCam.RAM_DISK} && mkdir skycam")
            os.system(f"cd {skyCam.RAM_DISK}/skycam && mkdir imgs")
      except Exception as e:
         print(e)
         exit(100)
      def __thread_tick(ffn: str):
         self.__take_img(ffn=ffn)
      # -- -- -- --
      while True:
         idx: int = rnd_q.get()
         fpath = f"{sky_cam_fld}/imgs/skycam_img_{idx:02}.jpg"
         __thread_tick(ffn=fpath)
         rnd_q.put(idx)
         time.sleep(skyCam.CAM_THREAD_TICK_MS)
      # -- -- -- --

   def __take_img(self, ffn: str):
      try:
         # -- -- -- --
         if os.path.exists(ffn):
            os.unlink(ffn)
         # -- -- -- --
         time.sleep(0.01)
         skyCam.CAM_LOCK.acquire()
         skyCam.CAM.capture_file(ffn, wait=True)
         skyCam.CAM_LOCK.release()
         # -- -- -- --
      except Exception as e:
         print(e)
      finally:
         self.img_cnt += 1
         if skyCam.CAM_LOCK.locked():
            skyCam.CAM_LOCK.release()
