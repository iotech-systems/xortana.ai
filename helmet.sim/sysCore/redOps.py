
import redis as _red
import configparser as _cp


class redOps(object):

   def __init__(self, ini: _cp.ConfigParser):
      self.ini: _cp.ConfigParser = ini
      self.host = self.ini.get("REDIS", "HOST")
      self.port = int(self.ini.get("REDIS", "PORT"))
      self.red: _red.Redis = \
         _red.Redis(host=self.host, port=self.port, decode_responses=True)

   def ping(self) -> bool:
      return self.red.ping()
