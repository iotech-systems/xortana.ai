
import threading, time
import adafruit_amg88xx
import busio, board


class sysThermals(object):

   RIGHT_I2C_ADDR: int = 0x68
   LEFT_I2C_ADDR: int = 0x69
   RIGHT_I2C_READ: bool = True
   LEFT_I2C_READ: bool = True

   def __init__(self):
      self.i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
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
      print(self.right_amg8833.pixels)
      print("-- [ start: right thermal frame ] --")
      for row in self.right_amg8833.pixels:
         print(["{0:.1f}".format(temp) for temp in row])
      print("-- [ end: right thermal frame ] --")


# -- testing --
if __name__ == "__main__":
   obj: sysThermals = sysThermals()
   obj.init()
