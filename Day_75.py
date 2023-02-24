"""
Python Text to Speech
----------------------
"""

from gtts import gTTS
import os
import time
import playsound

dir_path = os.path.dirname(os.path.realpath(__file__))
names = ["Rahul", "Nishant", "Harry"]

language = 'en'

count = 1
for text in names:
    myobj = gTTS(text=f"shout out {text}", lang=language, slow=False)
    myobj.save(f"{text}_{count}.mp3")
    count+=1

mp3files = [file for file in os.listdir() if file.endswith(".mp3")]

for file in mp3files:
    playsound.playsound(f"{dir_path}/{file}")
    os.remove(f"{dir_path}/{file}")
    time.sleep(1)


# OR
# ----


from os import system
for name in names:
    system(f"say Shoutout to {name} ")
