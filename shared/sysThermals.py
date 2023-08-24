
import threading, time
import adafruit_amg88xx
import busio, board


class sysThermals(object):

   RIGHT_I2C_ADDR: int = 0x68
   LEFT_I2C_ADDR: int = 0x69

   def __init__(self):
      self.i2c: busio.I2C = busio.I2C(board.SCL, board.SDA)
      self.right_amg8833 = adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.RIGHT_I2C_ADDR)
      self.left_amg8833 = adafruit_amg88xx.AMG88XX(self.i2c, sysThermals.LEFT_I2C_ADDR);
      self.amg8833_thread = threading.Thread(target=self.__amg8833_thread)

   def init(self):
      self.amg8833_thread.start()

   def __amg8833_thread(self):
      while True:
         self.__amg883_read_left()
         self.__amg883_read_right()
         time.sleep(0.2)

   def __amg883_read_left(self):
      pass

   def __amg883_read_right(self):
      print("-- [ start: right thermal frame ] --")
      for row in self.right_amg8833.pixels:
         print(["{0:.1f}".format(temp) for temp in row])
      print("-- [ end: right thermal frame ] --")


# -- testing --
if __name__ == "__main__":
   obj: sysThermals = sysThermals()
   obj.init()
