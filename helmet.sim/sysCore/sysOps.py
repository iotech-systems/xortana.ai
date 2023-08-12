
import os, configparser as _cp


class sysOps(object):

   def __init__(self, ini: _cp.ConfigParser):
      self.ini: _cp.ConfigParser = ini
      self.sim_root: str = ""

   def init(self) -> bool:
      # -- check ramfs --
      p = self.ini.get("RAMFS", "IOTECH_ROOT")
      if not os.path.exists(p):
         print(f"RAMFS_IOTECH_ROOT_NOT_EXIT: {p}")
         return False
      # -- -- -- --
      self.sim_root = self.ini.get("RAMFS", "SIMS_ROOT")
      if not os.path.exists(self.sim_root):
         os.makedirs(self.sim_root)
      # -- -- -- --
      return True

   def make_ramfs_path(self, path: str):
      path = path.strip('/')
      p = f"{self.sim_root}/{path}"
      os.mkdir(p)
      return os.path.exists(p)
