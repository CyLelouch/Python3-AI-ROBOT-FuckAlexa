         #Modules Needed
#gTTS
#SpeechRecognition
#playsound  --- must use playsound==1.2.2
#pyaudio
        #Importing Modules

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import webbrowser
        #Creating file and playing text from file via mp3 extension

print("starting")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

#Function for future commands -atm === Null;







#wake and starting test

WAKE = "robot"
print("Start")

while True:
    print("Listening")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()

#Hard Coded Commands Applied here

    

        #Greetings
        if "hello" in text:
            speak("hi there")

        if "hi" in text:
            speak("hello")
        
        if "hay" in text:
            speak("whats up")

        if "sup" in text:
            speak("sup with you dog")
        
        if "sap" in text:
            speak(" nothing much. you.")

# Stop program from continuation 

        if "nevermind" in text:
            print("stoping continuation ")

        #importingFilesTest
        if "file import" in text:
            speak("testing right now. one second.")
            import PythonImportingTest
            speak("testing completed. all good. Check print statement for confirmation ")
                
        #web browser searches 

        if "playlist" in text:
            webbrowser.open("https://www.youtube.com/watch?v=Jms3FCuuIos&list=PLfFBZBQAEaXmfDmDwIbT9Ug6EMNEmujhP&index=1")
        if "stop" in text:
            os.system("taskkill /im chrome.exe /f")
