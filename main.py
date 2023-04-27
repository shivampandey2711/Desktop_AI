import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('vioce', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good after noon")
    else:
           speak("good evening")

    speak("Hello Sir i am jarvis. please tell me how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
         print("recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said: {query}\n")

    except Exception as e:
           #print(e)
           print("say that again please....")
           return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ziddiboy2711@gmail.com', 'ziddiboy#271123')
    server.sendmail('ziddiboy2711@gmail.com', to, content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
             speak('searching wikipedia....')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             print(results)
             speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\infinx\\SONG'
            song = os.listdir(music_dir)
            #print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'visual studio' in query:
          codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

        elif 'firefox' in query:
          codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
          os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "yougeshawasthi35@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("sorry sir . I am not able to send this  email")
