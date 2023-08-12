
import setproctitle
import datetime, redis
import time, configparser as _cp
from sensorCore.sensorInterface import sensorInterface as _iS
from sysCore.redOps import redOps
from sysCore.sysOps import sysOps
from shared.sim_strgs import redStrings


SIGNAL_SYNC = "SENSOR_SYNC"


class sensorGEN_v0(_iS):

   def __init__(self, sec: _cp.SectionProxy):
      super().__init__()
      # -- -- -- --
      self.sec: _cp.SectionProxy = sec
      self.ini_id = self.sec.get("ID")
      self.ini_lbl = self.sec.get("LBL")
      self.args: str = self.sec.get("ARGS")
      # -- -- -- --
      self.tag: str = f"{self.ini_lbl}_{self.ini_id}"
      self.audio_tag: str = f"AUDIO_BUFFER_{self.ini_id}"
      self.sys_signal: int = 1
      self.dts: str = str(datetime.datetime.utcnow())
      self.rops: redOps = None
      self.sosp: sysOps = None
      self.rpubsub = None

   def init(self, sOps: sysOps, rOps: redOps):
      try:
         # -- --
         self.sosp = sOps
         self.rops = rOps
         # -- --
         d: {} = {"START_DTS": self.dts}
         self.rops.red.select(1)
         self.rops.red.hset(name=self.tag, mapping=d)
         self.rops.red.select(2)
         self.rops.red.set(name=self.audio_tag, value=bytes([0, 0, 0, 0]))
         self.rpubsub = self.rops.red.pubsub()
         self.rpubsub.psubscribe(**{redStrings.SENSOR_SYNC_PULSE: self.__on_signal_sync})
         self.rpubsub.run_in_thread(sleep_time=0.2)
         # -- ramfs --
         path: str = f"sound_{self.ini_lbl}"
         if not self.sosp.make_ramfs_path(path):
            print(f"UnableToMakePath: {path}")
      except Exception as e:
         print(e)

   def entry_point(self):
      t: str = f"xor.{self.ini_lbl}"
      setproctitle.setproctitle(t)
      while self.sys_signal == 1:
         print(self.tag)
         time.sleep(4.0)

   def set_red(self, red: redis.Redis):
      self.rops: redis.Redis = red

   def __on_signal_sync(self, msg):
      print(msg)
