import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from sound import sound

def speak(str):
    tts = gTTS(text=str,lang='en')
    tts.save("voice.mp3")
    sound()
