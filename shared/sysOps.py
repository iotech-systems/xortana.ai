
import os
from stat import S_ISREG, ST_MODE, ST_CTIME


class sysOps(object):

   @staticmethod
   def folder_files(fpath: str) -> (int, []):
      #  -- -- -- --
      def _sort_func(i) -> int:
         return int(i[1])
      #  -- -- -- --
      try:
         print(f"folder_files: {fpath}")
         if not os.path.exists(fpath):
            return 1, None
         # -- -- -- --
         fls = os.listdir(fpath)
         ffps = [(fn, os.stat(f"{fpath}/{fn}")[ST_CTIME]) for fn in fls]
         ffps_sorted = sorted(ffps, key=_sort_func, reverse=True)
         # -- -- -- --
         return 0, ffps_sorted
      except Exception as e:
         return 2, f"{e}"
