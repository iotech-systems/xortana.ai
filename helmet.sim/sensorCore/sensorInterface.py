
import abc, multiprocessing
from sysCore.sysOps import sysOps
from sysCore.redOps import redOps


class sensorInterface(multiprocessing.Process):

   def __init__(self):
      super().__init__(target=self.entry_point)

   @abc.abstractmethod
   def init(self, sOps: sysOps, rOps: redOps):
      pass

   @abc.abstractmethod
   def entry_point(self):
      pass
