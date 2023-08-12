
import configparser as _cp
from sensorCore.sensorGENv0 import sensorGEN_v0
from sensorCore.sensorCAM_VL_v0 import sensorCAM_VL_v0


class botCreator(object):

   def __init__(self, ini: _cp.ConfigParser):
      self.ini: _cp.ConfigParser = ini
      self.bot_secs: [str] = None
      self.bots: [] = None

   def create(self, sensor_sec) -> []:
      tmp: str = self.ini.get("SYSTEM", sensor_sec)
      sensor_secs = [s.strip() for s in tmp.split(",")]
      bots: [] = [self.__create_bot(sec) for sec in sensor_secs]
      return bots

   def __create_bot(self, bot_sec: str) -> [None, object]:
      _sec: _cp.SectionProxy = self.ini[bot_sec]
      _type = _sec.get("TYPE")
      # -- -- -- --
      if _type == "GENv0":
         bot = self.__gen_v0(_sec)
      elif _type == "CAM_VL_v0":
         bot = self.__cam_v0(_sec)
      else:
         bot = None
      # -- -- -- --
      return bot

   def __gen_v0(self, sec: _cp.SectionProxy):
      return sensorGEN_v0(sec)

   def __cam_v0(self, sec: _cp.SectionProxy):
      return sensorCAM_VL_v0(sec)
