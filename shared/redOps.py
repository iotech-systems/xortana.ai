
import redis, json
try:
   from shared.datatypes import redDBIdx
except ModuleNotFoundError:
   from datatypes import redDBIdx
finally:
   pass


class redOps(redis.Redis):

   def __init__(self):
      super().__init__(host="localhost", port=6379)

   def save_thermal_read(self, read_key: str, arr: []):
      self.select(redDBIdx.THERMAL.value)
      if self.set(name=read_key, value=json.dumps(arr)):
         self.pexpire(read_key, 2000)
      # -- -- -- --
