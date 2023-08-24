
import busio, board
import threading, time
import adafruit_amg88xx
# -- core --
try:
   from shared.redOps import redOps
except ModuleNotFoundError:
   from redOps import redOps
finally:
   pass


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
      d: {} = {"LEFT_FRQ": self.FRAME_FREQ, "RIGHT_FREQ": self.FRAME_FREQ}
      key: str = "AMG8833_CONFIG"
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
      self.red.save_thermal_read(read_key, idx, self.left_amg8833.pixels)

   def __amg883_read_right(self):
      if self.right_amg8833 is None:
         return
      idx = sysThermals.__next_idx()
      read_key: str = f"RIGHT_AMG8833_{idx}"
      self.red.save_thermal_read(read_key, idx, self.right_amg8833.pixels)

   @staticmethod
   def __next_idx() -> str:
      key = f"{sysThermals.READ_COUNTER:08}"
      sysThermals.READ_COUNTER += 1
      return key


# -- -- -- -- [ testing ] -- -- -- --
if __name__ == "__main__":
   obj: sysThermals = sysThermals()
   obj.init()
