
import redis
import configparser as _cp
import time, threading as _th
import multiprocessing as _mp
# -- -- system -- --
from sysCore.redOps import redOps
from sysCore.sysOps import sysOps
from shared.sim_strgs import *


class xortanaAI(_mp.Process):

   TICK_DELAY: int = 1.0

   def __init__(self, INI_BOTS: _cp.ConfigParser, RED_OPS: redOps, SYS_OPS: sysOps):
      super().__init__(target=self.__entry_point)
      self.ini_bots: _cp.ConfigParser = INI_BOTS
      self.rops: redOps = RED_OPS
      self.sops: sysOps = SYS_OPS
      self.thr_sync: _th.Thread = _th.Thread(target=self.__thread_sync)

   def init(self) -> bool:
      return True

   def __entry_point(self):
      # -- threads inits --
      self.thr_sync.start()
      # -- start --
      while True:
         # print("xorai tick...")
         time.sleep(xortanaAI.TICK_DELAY)

   def __thread_sync(self):
      cnt: int = 0
      while True:
         try:
            self.rops.red.publish(redStrings.SENSOR_SYNC_PULSE, f"MSG_CNT: {cnt}")
            time.sleep(1.0)
            cnt += 1
         except Exception as e:
            print(e)
