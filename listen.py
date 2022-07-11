import os 
import time
import playsound
import SpeechRecognition as sr



def get_audio():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognize.listen(source)
        text = ""

        try:
            text = recognize.recognize_google(audio)
            print(text)
        
        except Exception as e:
            print("Exception: " + str(e) )

    return text
