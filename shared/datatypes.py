
import enum
import json


RUN_PATH: str = "/run/xora.ai"


class tickCode(enum.IntEnum):
   OK = 0,
   Error = 1

class redDBIdx(enum.IntEnum):
   CONFIG = 0
   THERMAL = 4


class execResult(object):

   def __init__(self, err: int, buff: str):
      self.err: int = err
      self.buff: str = buff

   def __str__(self):
      return self.toJson()

   def toJson(self):
      return json.dumps(self, default=lambda this: this.__dict__)


class sysPaths(object):

   SKYCAM_PEEK_LOCK_FILE: str = f"{RUN_PATH}/skycam/peek.sync"