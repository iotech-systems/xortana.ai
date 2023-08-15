#!/usr/bin/env python3

import time
from apps.xoraCams.cams.topCam import topCam


MAIN_TICK_SLEEP: float = 4.0
TOP_CAM: topCam = topCam()


def main():
   def __main_tick():
      print("run_cams: __main_tick()")
   # -- main ticks --
   while True:
      __main_tick()
      time.sleep(MAIN_TICK_SLEEP)


# -- -- -- entry point -- -- --
if __name__ == "__main__":
   main()
