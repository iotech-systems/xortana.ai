
import os


class sysOps(object):

   @staticmethod
   def folder_files(fpath: str) -> (int, []):
      try:
         print(f"folder_files: {fpath}")
         if not os.path.exists(fpath):
            return 1, None
         fls = os.listdir(fpath)
         return 0, fls
      except Exception as e:
         return 2, f"{e}"
