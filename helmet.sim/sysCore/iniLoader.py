
import sys
import configparser as _cp
from sysCore.sysOps import sysOps
from sysCore.redOps import redOps


def load_inis() -> ():
   # -- -- -- --
   INI_PATH: str = "conf/sensor_bots.ini"
   INI_BOTS: _cp.ConfigParser = _cp.ConfigParser()
   if len(INI_BOTS.read(INI_PATH)) != 1:
      print(f"IniLoadError: {INI_PATH}")
   # -- -- -- --
   INI_PATH = "conf/redis.ini"
   INI_REDIS: _cp.ConfigParser = _cp.ConfigParser()
   if len(INI_REDIS.read(INI_PATH)) != 1:
      print(f"IniLoadError: {INI_PATH}")
   RED_OPS: redOps = redOps(ini=INI_REDIS)
   if not RED_OPS.ping():
      print("BadRedPing")
      sys.exit(1)
   # -- -- -- --
   INI_PATH = "conf/sys.ini"
   INI_SYS: _cp.ConfigParser = _cp.ConfigParser()
   if len(INI_SYS.read(INI_PATH)) != 1:
      print(f"IniLoadError: {INI_PATH}")
   SYS_OPS: sysOps = sysOps(INI_SYS)
   if not SYS_OPS.init():
      print("UnableToInitSystem")
      exit(1)
   # -- -- -- --
   return INI_BOTS, RED_OPS, SYS_OPS

