from importlib import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from test import *
import requests
from bs4 import BeautifulSoup
import pyjokes

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning PG")

    elif hour>=12 and hour<18:
        speak("Good Afternoon PG")   

    else:
        speak("Good Evening PG") 
    speak("I am Friiday. Please tell me how may I help you") 
    
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,1.2)
        r.pause_threshold = 1
        print("listening........")
        audio = r.listen(source)
    try:
        print("Recognizing........")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say it again please....")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prashikgavali500@gmail.com','Saad@1234')
    server.sendmail('geniusnobita2604@gmail.com',to,content)
    server.close()

if __name__=="__main__":   
    while True:
        wishMe()
        query = takecommand().lower()
        if 'friday'in query:
            wishMe()
            while True:
                query= takecommand().lower()
            # logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('searching wikipedia')
                    query = query.replace('wikipedia',"")
                    results = wikipedia.summary(query,sentences=2)
                    speak('According to wikipedia..')
                    print(results)
                    speak(results)
                # elif "temperature" in query:

                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')
                    if 'close youtube' in query:
                        webbrowser.open('youtube.com')
                elif 'open google' in query: 
                    webbrowser.open('google.com')
                elif 'open stackoverflow' in query:
                    webbrowser.open('stackoverflow.com')
                elif 'play music' in query:
                    music_dir = 'C:\\Users\\Hp\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,random.choice(songs)))
                elif 'time' in query:
                    strTime=datetime.datetime.now().strftime('%H'"hour"'%M'"minutes"'%S'"seconds")
                    speak(f"sir,the time is{strTime}")
                elif 'joke' in  query:
                    speak(pyjokes.get_joke())
                elif 'open vs code' in query:
                    path="C:\\Users\\Sonu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(path)
                elif 'open chrome' in query:
                    path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                    os.startfile(path)
                elif 'email to ' in query:
                    try:
                        speak ("what should i say?")
                        content=takecommand()
                        to='geniusnobita2604@gmail.com'
                        sendEmail(to,content)
                        speak('email has been sent!')
                    except Exception as e:
                        print(e)
                        speak('sorry my friend Prashik. i am unable to send this email ')
                elif 'your developer' in query:
                    speak("PG is my developer.") 
                elif "what's my name" in query:
                    speak("PG") 
                elif 'temperature' in query:
                    search='temperature in Kolhapur'
                    url=f"https://www.google.com/search?q={search}"
                    x=requests.get(url)
                    data=BeautifulSoup(x.text,'html.parser')
                    temp= data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    # remember= open("Remember.txt", "x")
                    remember = open("Remember.txt","w+")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember =open("Remember.txt", "x")
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read()) 
                elif "search" in query and "google" in query:
                    query = query.replace("search","")
                    query = query.replace("on google","")
                    query = query.replace("google","")
                    string = query.split()
                    search = ""
                    for i in string:
                        search += i
                        search += "+"
                    webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")

                elif "search" in query and "youtube" in query :
                        query = query.replace("search","")
                        query = query.replace("on youtube","")
                        query = query.replace("youtube","")
                        string = query.split()
                        search = ""
                        for i in string:
                            search += i
                            search += "+"
                        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                elif 'goodbye jack' in query:
                    speak('thanks for using me have a good day')
                    exit(0)
                else:
                    print("sorry,i unable to answer this task")
