
import enum
import json


class tickCode(enum.IntEnum):
   OK = 0,
   Error = 1


class execResult(object):

   def __init__(self, err: int, buff: str):
      self.err: int = err
      self.buff: str = buff

   def __str__(self):
      return self.toJson()

   def toJson(self):
      return json.dumps(self, default=lambda this: this.__dict__)
