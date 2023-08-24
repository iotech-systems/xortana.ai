
import redis
from shared.datatypes import redDBIdx


class redOps(redis.Redis):

   def __init__(self):
      super().__init__(host="localhost", port=6379)

   def save_thermal_read(self, read_key: str, arr: []):
      self.select(redDBIdx.THERMAL)
      if self.set(name=read_key, value=arr):
         self.pexpire(read_key, 2000)
      # -- -- -- --
