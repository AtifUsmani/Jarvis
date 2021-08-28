import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import yt

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic buiding for tasks

        if "open brave" in query:
            path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(path)

        elif "open command prompt in query":
            os.system("start cmd")

        elif "open Camera" in query:
            cap = cv2.VideoCapture(8)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        if "play music" in query:
            pass