#!/usr/bin/env python3

import busio, board
import threading, time
import adafruit_amg88xx
# -- core --
try:
   from shared.redOps import redOps
   from shared.sysTTS import sysTTS
except ModuleNotFoundError:
   from redOps import redOps
   from sysTTS import SYS_TTS
finally:
   pass

triggers: {} = {"level0": {48, 34.0}, "level1": {32, 32.0}
   , "level2": {16, 30.0}}


class sysThermals(object):

   FRAME_FREQ: int = 5
   FRAME_TICK_INTERVAL: float = (1 / FRAME_FREQ)
   READ_COUNTER: int = 0
   RIGHT_I2C_ADDR: int = 0x68
   LEFT_I2C_ADDR: int = 0x69
   RIGHT_I2C_READ: bool = True
   LEFT_I2C_READ: bool = True

   def __init__(self):
      # -- -- -- --
      self.i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
      self.red: redOps = redOps()
      # -- -- -- --
      try:
         self.right_amg8833 = None
         self.right_amg8833 = (
            adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.RIGHT_I2C_ADDR))
      except Exception as e:
         sysThermals.RIGHT_I2C_READ = False
         print(e)
      finally:
         pass
      # -- -- -- --
      try:
         self.left_amg8833 = None
         self.left_amg8833 = (
            adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.LEFT_I2C_ADDR))
      except Exception as e:
         sysThermals.LEFT_I2C_ADDR = False
         print(e)
      # -- -- -- --
      key: str = "AMG8833_CONFIG"
      d: {} = {"FRAME_FREQ": self.FRAME_FREQ}
      self.red.save_thermal_config(key, d)
      # -- -- -- --
      self.amg8833_thread = threading.Thread(target=self.__amg8833_thread)

   def init(self):
      if not self.red.ping():
         print("[ NoRedPong ]")
      self.amg8833_thread.start()

   def __amg8833_thread(self):
      def __tick() -> int:
         try:
            if sysThermals.LEFT_I2C_READ:
               self.__amg883_read_left()
            if sysThermals.RIGHT_I2C_READ:
               self.__amg883_read_right()
            return 0
         except Exception as e:
            print(e)
            return 1
      # -- -- -- --
      while True:
         if __tick() == 0:
            time.sleep(sysThermals.FRAME_TICK_INTERVAL)
         else:
            time.sleep(1.0)

   def __amg883_read_left(self):
      if self.left_amg8833 is None:
         return
      idx = sysThermals.__next_idx()
      read_key: str = f"LEFT_AMG8833_{idx}"
      pixels: [] = self.left_amg8833.pixels
      self.red.save_thermal_read(read_key, idx, pixels)
      self.__check_for_triggers(pixels, "left")

   def __amg883_read_right(self):
      if self.right_amg8833 is None:
         return
      idx = sysThermals.__next_idx()
      read_key: str = f"RIGHT_AMG8833_{idx}"
      pixels: [] = self.right_amg8833.pixels
      self.red.save_thermal_read(read_key, idx, pixels)
      self.__check_for_triggers(pixels, "right")

   def __check_for_triggers(self, pix_tbl, side: str):
      # check level 1 - very close heat souce
      accu: int = 0
      # -- -- -- -- --
      cnt, temp = triggers["level0"]
      for row in pix_tbl:
         accu += len([c for c in row if float(c) >= temp])
      if accu >= cnt:
         SYS_TTS.say(f"John, level zero thermal on the {side}.")
         print("thermal trigger level0")
         print(triggers["level0"])
         return
      # -- -- -- -- --
      cnt, temp = triggers["level1"]
      for row in pix_tbl:
         accu += len([c for c in row if float(c) >= temp])
      if accu >= cnt:
         SYS_TTS.say(f"John, level one thermal on the {side}.")
         print("thermal trigger level1")
         print(triggers["level1"])

         return
      # -- -- -- -- --
      cnt, temp = triggers["level2"]
      for row in pix_tbl:
         accu += len([c for c in row if float(c) >= temp])
      if accu >= cnt:
         SYS_TTS.say(f"John, level two thermal on the {side}.")
         print("thermal trigger level2")
         print(triggers["level2"])
         return
      # -- -- -- -- --
      return

   @staticmethod
   def __next_idx() -> str:
      key = f"{sysThermals.READ_COUNTER:08}"
      sysThermals.READ_COUNTER += 1
      return key


# -- -- -- -- [ testing ] -- -- -- --
if __name__ == "__main__":
   obj: sysThermals = sysThermals()
   obj.init()
