#!/usr/bin/env python3

import pyttsx3

eng = pyttsx3.init()
voices = eng.getProperty('voices')
for v in voices:
    if v.gender != "male":
      print(v)
