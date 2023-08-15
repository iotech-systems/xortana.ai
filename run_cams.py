#!/usr/bin/env python3

import time
from apps.xoraCams.cams.topCam import topCam
from apps.shared.core.datatypes import *


MAIN_TICK_SLEEP: float = 4.0
TOP_CAM: topCam = topCam()


def init():
   TOP_CAM.start()

def main():
   # -- init code --
   init()
   # -- man tick --
   def __main_tick() -> tickCode:
      print("run_cams: __main_tick()")
      return tickCode.OK
   # -- main loop --
   while True:
      tick_code: tickCode = __main_tick()
      time.sleep(MAIN_TICK_SLEEP)


# -- -- -- entry point -- -- --
if __name__ == "__main__":
   print("\n\t-- [ main ] --\n")
   main()
