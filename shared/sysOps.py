
import os


class sysOps(object):

   @staticmethod
   def folder_files(fpath: str) -> (int, []):
      try:
         print(f"folder_files: {fpath}")
         if not os.path.exists(fpath):
            return 1, None
         fls = os.listdir(fpath)
         ffps = [(fn, os.stat(f"{fpath}/fn")) for fn in fls]
         print(ffps)
         return 0, fls
      except Exception as e:
         return 2, f"{e}"
