
import os.path, time
import pyaudio, wave


class sysSnd(object):

   WAVE_FILE: str = ""
   SND_CARD_INDEX: int = 0
   TONES_PATH: str = "/opt/xortana.ai/sounds/tones"
   # PY_AUDIO: pyaudio.PyAudio = pyaudio.PyAudio()
   CHNK_SIZE: int = 1024

   @staticmethod
   def play_tone(wav_name: str, cnt: int = 1):
      stream: pyaudio.Stream = None
      PY_AUDIO: pyaudio.PyAudio = None
      try:
         ffpath: str = f"{sysSnd.TONES_PATH}/{wav_name}.wav"
         if not os.path.exists(ffpath):
            print(f"FileNotFound: {ffpath}")
            return
         wave_fl_obj = wave.open(ffpath, "rb")
         chnls: int = wave_fl_obj.getnchannels()
         rate = wave_fl_obj.getframerate()
         PY_AUDIO = pyaudio.PyAudio()
         _format = PY_AUDIO.get_format_from_width(wave_fl_obj.getsampwidth())
         stream = PY_AUDIO.open(format=_format, channels=chnls, rate=rate, output=True)
         # -- -- -- --
         while cnt > 0:
            print(f"play_tone: {wav_name}")
            wave_fl_obj.rewind()
            wave_data = wave_fl_obj.readframes(sysSnd.CHNK_SIZE)
            while wave_data != b'':
               stream.write(wave_data)
               wave_data = wave_fl_obj.readframes(sysSnd.CHNK_SIZE)
            cnt -= 1
            if cnt > 0:
               time.sleep(0.500)
      except Exception as e:
         print(e)
      finally:
         try:
            PY_AUDIO.close(stream)
         except:
            pass
