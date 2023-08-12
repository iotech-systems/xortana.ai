

from sensorCore.sensorInterface import sensorInterface as _SI_


class genSensor(_SI_):
   # __slots__ = ["sensor_lbl"]

   def __init__(self, locID: str, lbl: str):
      self.locID: str = locID
      self.sensor_lbl: str = lbl

   def init(self):
      pass
