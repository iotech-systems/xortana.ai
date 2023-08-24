
import redis, json
try:
   from shared.datatypes import redDBIdx
except ModuleNotFoundError:
   from datatypes import redDBIdx
finally:
   pass


class redOps(redis.Redis):

   def __init__(self):
      super().__init__(host="localhost", port=6379, decode_responses=True)

   def save_thermal_read(self, read_key: str, idx: str, arr: []):
      self.select(redDBIdx.THERMAL.value)
      val: str = f"{idx}::{json.dumps(arr)}"
      if self.set(name=read_key, value=val):
         self.pexpire(read_key, 2000)
      # -- -- -- --

   def save_thermal_config(self, hash_name, d: {}):
      self.hset(name=hash_name, mapping=d)

   def read_thermal_reads(self) -> {}:
      self.select(redDBIdx.THERMAL.value)
      # -- -- -- --
      left_keys = self.keys(f"LEFT_AMG8833_*")
      left_vals = self.mget(left_keys)
      right_keys = self.keys(f"RIGHT_AMG8833_*")
      right_vals = self.mget(right_keys)
      # -- -- -- --
      return {"LEFT": left_vals, "RIGHT": right_vals}
