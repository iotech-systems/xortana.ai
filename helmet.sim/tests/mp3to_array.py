#!/usr/bin/env python3

import pydub
import numpy as np


def read(f, normalized=False):
   """MP3 to numpy array"""
   a = pydub.AudioSegment.from_mp3(f)
   y = np.array(a.get_array_of_samples())
   if a.channels == 2:
      y = y.reshape((-1, 2))
   if normalized:
      return a.frame_rate, np.float32(y) / 2 ** 15
   else:
      return a.frame_rate, y


def write(f, sr, x, normalized=False):
   """numpy array to MP3"""
   channels = 1 # 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
   if normalized:  # normalized array - each item should be a float in [-1, 1)
      y = np.int16(x * 2 ** 15)
   else:
      y = np.int16(x)
   song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
   song.export(f, format="mp3", bitrate="32k")


# audio_file = '../input/birdsong-recognition/train_audio/aldfly/XC134874.mp3'
audio_file = "../../data/guns/m16/m16auto_1s.mp3"
sr, x = read(audio_file)

import matplotlib.pyplot as plt

plt.figure(figsize=(16, 10))
plt.plot(x)
plt.title("Sample MP3 loading into Numpy")
plt.show()
print("xxx")
