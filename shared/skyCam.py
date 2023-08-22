
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
      if not os.path.exists(skyCam.RAM_DISK):
         os.makedirs(skyCam.RAM_DISK)
      if skyCam.__inst is None:
         skyCam.__inst = skyCam()
      # -- -- -- --
      return skyCam.__inst

   def __init__(self):
      if skyCam.CAM is None:
         skyCam.CAM = PiCam2()
         conf = skyCam.CAM.create_still_configuration(main={"size": (1920, 1080)})
         skyCam.CAM.configure(conf)
      self.cam_thread: threading.Thread = threading.Thread(target=self.__cam_thread)

   def start_cam_thread(self):
      self.cam_thread.start()

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
         SYS_TTS.say("New image in 3", 150)
         time.sleep(0.36)
         SYS_TTS.say("2", 150)
         time.sleep(0.36)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         self.__take_img(ffn)
         skyCam.prefixIdx[prefix] = (idx + 1)
         if os.path.exists(ffn):
            img: Image = Image.open(ffn)
            img.thumbnail((324, 243))
            img.save(f"{skyCam.TF_THUMS_FOLDER}/thm_{img_name}")
            SYS_TTS.say("Image has been taken", 150)
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

   def __cam_thread(self):
      # -- -- -- --
      rnd_q: queue.SimpleQueue = queue.SimpleQueue()
      [rnd_q.put(i) for i in range(0, 8)]
      sky_cam_fld: str = f"{skyCam.RAM_DISK}/skycam"
      try:
         if not os.path.exists(sky_cam_fld):
            os.system(f"cd {skyCam.RAM_DISK} && mkdir -p skycam/imgs")
      except Exception as e:
         print(e)
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
         skyCam.CAM_LOCK.acquire()
         skyCam.CAM.start_and_capture_file(ffn, show_preview=False)
         skyCam.CAM_LOCK.release()
      except Exception as e:
         print(e)
      finally:
         if skyCam.CAM_LOCK.locked():
            skyCam.CAM_LOCK.release()
