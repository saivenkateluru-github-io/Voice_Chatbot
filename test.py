from speak import speak
from listen import get_audio

speak("hello")
print("say something")
text = get_audio()

if "hello" in text:
    print("how are you ?")
    speak("how are you ?")




