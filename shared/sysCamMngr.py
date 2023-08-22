
import threading
from shared.skyCam import skyCam


class sysCamMngr(object):

   def __init__(self):
      self.sky_cam: skyCam = skyCam.Instance()
