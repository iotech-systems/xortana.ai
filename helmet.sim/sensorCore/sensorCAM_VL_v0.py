
import time, redis, configparser as _cp
from sensorCore.sensorInterface import sensorInterface as _iS


class sensorCAM_VL_v0(_iS):

   def __init__(self, sec: _cp.SectionProxy):
      super().__init__()
      self.sec: _cp.SectionProxy = sec
      self.red: redis.Redis = None

   def init(self):
      pass

   def entry_point(self):
      while True:
         print("sensorCAM_VL_v0")
         time.sleep(8.0)

   def set_red(self, red: redis.Redis):
      self.red = red
