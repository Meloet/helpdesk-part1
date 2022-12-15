import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Melo")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon Melo")
    elif hour>=16 and hour<=23:
        speak("Good Evening Melo")
    speak("How can I help you?")
if(__name__=='__main__'):
    wishme()