
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()

# Microphone initialization
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)


def talk(query):
    engine.say(query)
    engine.runAndWait()


def recognize_speech():
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source, 60, 10)
        print("Recognizing...")
        return recognizer.recognize_google(audio)


def execute_command(query):
    if "hello" in query:
        talk("hello i am bot, how can i assist you")
    elif "play" in query:
        kit.playonyt(query)
    elif "search" in query or "define" in query:
        keywords = query.split("search")[-1].split("define")[-1].strip()
        text = wikipedia.summary(keywords)
        talk(text)
        talk("For your convenience, I am printing it on the screen sir.")
        print(text)
    elif "open command prompt" in query or "open cmd" in query:
        open_cmd()
    elif "open calculator" in query:
        open_calculator()
    elif "open camera" in query:
        open_camera()
    elif "open Notepad" in query:
        open_notepad()
    elif "stop" in query:
        return True


def open_calculator():
    os.system("calc")


def open_cmd():
    os.system("cmd")


def open_camera():
    os.system("start microsoft.windows.camera:")


def open_notepad():
    os.system("notepad")


try:
    while True:
        query = recognize_speech()
        print("You said:", query)

        if execute_command(query):
            break

except sr.UnknownValueError:
    print("Sorry, could not understand audio.")

except sr.RequestError as e:
    print(f"Error with the speech recognition service; {e}")

except wikipedia.exceptions.PageError as pe:
    print(f"Error with Wikipedia: {pe}")
