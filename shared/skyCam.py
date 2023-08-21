
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
   TF_IMGS_FOLDER: str = "/opt/xortana.ai/tf/imgs"
   TF_THUMS_FOLDER: str = "/opt/xortana.ai/tf/thums"
   RAM_DISK: str = "/run/xora.si/skycam"
   CAM_LOCK: threading.Lock = threading.Lock()

   def __init__(self, act: str, args: str):
      self.act: str = act
      self.args: str = args
      if skyCam.CAM is None:
         skyCam.CAM = PiCam2()
      # -- tf thread --
      self.tf_thread: threading.Thread = threading.Thread(target=self.__cam_thread)

   def init(self):
      # -- -- -- --
      if os.path.exists(skyCam.RAM_DISK):
         os.makedirs(skyCam.RAM_DISK)
      # -- -- -- --
      self.tf_thread.start()

   def execute(self) -> execResult:
      if self.act == "take_img":
         self.__take_img(self.args)
      # -- -- -- --
      rval: execResult = execResult(0, "OK")
      return rval

   """
      this tread will run tensorflow code on skycam every conf_ms
   """
   def __cam_thread(self):
      # -- -- -- --
      rnd_q: queue.SimpleQueue = queue.SimpleQueue()
      [rnd_q.put(i) for i in range(0, 8)]
      def __thread_tick(ffn: str):
         skyCam.CAM_LOCK.acquire()
         skyCam.CAM.start_and_capture_file(ffn, show_preview=False)
         skyCam.CAM_LOCK.release()
      # -- -- -- --
      while True:
         idx: int = rnd_q.get()
         fpath = f"{skyCam.RAM_DISK}/skycam/img_{idx:02}.jpg"
         __thread_tick(ffn=fpath)
         rnd_q.put(idx)
         time.sleep(skyCam.CAM_THREAD_TICK_MS)
      # -- -- -- --

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
         time.sleep(0.36)
         SYS_TTS.say("2", 150)
         time.sleep(0.36)
         SYS_TTS.say("1", 150)
         # -- -- -- --
         skyCam.CAM_LOCK.acquire()
         skyCam.CAM.start_and_capture_file(ffn, show_preview=False)
         skyCam.CAM_LOCK.release()
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
      finally:
         try:
            if skyCam.CAM_LOCK.locked():
               skyCam.CAM_LOCK.release()
         except Exception as e:
            print(e)
