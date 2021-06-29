import os
import smtplib

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    speak("I Am Rajesh sir, How May I help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User Said:", query)
    except Exception as e:
        print(e)
        print("Please speak again....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("webdeveloper0129@gmail.com", "Abhi@Amit")
    server.sendmail("webdeveloper0129@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    # speak("Hello Rajesh")
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "E:\\Music\\Gurnam Bhullar"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(str_time)
            speak(f"Sir, The Time is:{str_time}")
        elif "open chrome" in query:
            path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(path)
        elif 'mail to me' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "bhambhusaab0029@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Abhi email is not sent")
