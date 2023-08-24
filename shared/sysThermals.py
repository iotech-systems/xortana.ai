
import busio, board
import threading, time
import adafruit_amg88xx
# -- core --
try:
   from shared.redOps import redOps
except:
   from redOps import redOps
finally:
   pass


class sysThermals(object):

   READ_COUNTER: int = 0
   RIGHT_I2C_ADDR: int = 0x68
   LEFT_I2C_ADDR: int = 0x69
   RIGHT_I2C_READ: bool = True
   LEFT_I2C_READ: bool = True

   def __init__(self):
      self.i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
      self.red: redOps = redOps()
      try:
         self.right_amg8833 = (
            adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.RIGHT_I2C_ADDR))
      except Exception as e:
         sysThermals.RIGHT_I2C_READ = False
         print(e)
      try:
         self.left_amg8833 = (
            adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.LEFT_I2C_ADDR))
      except Exception as e:
         sysThermals.LEFT_I2C_ADDR = False
         print(e)
      self.amg8833_thread = threading.Thread(target=self.__amg8833_thread)

   def init(self):
      if not self.red.ping():
         print("[ NoRedPong ]")
      self.amg8833_thread.start()

   def __amg8833_thread(self):
      while True:
         if sysThermals.LEFT_I2C_READ:
            self.__amg883_read_left()
         if sysThermals.RIGHT_I2C_READ:
            self.__amg883_read_right()
         time.sleep(0.2)

   def __amg883_read_left(self):
      pass

   def __amg883_read_right(self):
      idx = self.__next_idx()
      read_key: str = f"RIGHT_AMG8833_{idx}"
      self.red.save_thermal_read(read_key, self.right_amg8833.pixels)

   def __next_idx(self) -> str:
      key = f"{sysThermals.READ_COUNTER:06}"
      sysThermals.READ_COUNTER += 1
      return key


# -- testing --
if __name__ == "__main__":
   obj: sysThermals = sysThermals()
   obj.init()
