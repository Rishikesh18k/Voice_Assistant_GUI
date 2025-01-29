import pyttsx3
import webbrowser     # pip install webbrowser
import datetime
import requests
from bs4 import BeautifulSoup  # pip install bs4
import wikipedia        # pip install wikipedia
import eel
import pyautogui
import time

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()


def Time(query):
    if f"time".lower() in query.lower():
        strtime = datetime.datetime.now().strftime("%H:%M")
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            print(f"The time is - "+strtime+ "AM")
            eel.DisplayMessage("The time is - "+strtime+ "AM")
            speak(f"The time is "+strtime+ "AM")
        else:
            print(f"The time is - "+strtime+ "PM")
            eel.DisplayMessage("The time is - "+strtime+ "PM")
            speak(f"The time is "+strtime+ "PM")


def SearchOnYouTube(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("youtube","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening YouTube")
        speak(f"Opening YouTube")
        web = "https://www.youtube.com/search?q=" + query
        webbrowser.open(web)


def SearchOnGoogle(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Google")
        speak(f"Opening Google")
        web = "https://www.google.com/search?q=" + query
        webbrowser.open(web)

def SearchLocation(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("location","")
        query = query.replace("locati","")
        query = query.replace("map","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Google Map")
        speak(f"Opening Google Map")
        web = "https://www.google.com/maps/dir/" + query
        webbrowser.open(web)


def SearchOnWikipedia(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("wikipedia","")
        query = query.replace("to","")
        query = query.replace("according","")
        result = wikipedia.summary(query, sentences=2)
        eel.DisplayMessage("According to wikipedia")
        speak("According to wikipedia")
        print(">>> "+result)
        eel.DisplayMessage(result)
        speak(result)

def SearchVideo(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("play","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Web")
        speak(f"Opening web")
        web = "https://www.google.com/search?q=" + query
        webbrowser.open(web)

def SearchPhoto(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Web")
        speak(f"Opening web")
        web = "https://www.google.com/search?q=" + query
        webbrowser.open(web)

def SearchGame(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Web")
        speak(f"Opening web")
        web = "https://www.google.com/search?q=" + query
        webbrowser.open(web)

def SearchMusic(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        query = query.replace("youtube","")
        eel.DisplayMessage("Opening YouTube")
        speak(f"Opening YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def SearchWallpaper(query):
        query = query.replace("jarvis","")
        query = query.replace("open","")
        query = query.replace("on","")
        query = query.replace("google","")
        query = query.replace("to","")
        query = query.replace("according","")
        eel.DisplayMessage("Opening Web")
        speak(f"Opening web")
        web = "https://www.google.com/search?q=" + query
        webbrowser.open(web)

def FindDate(query):
        query = query.replace("jarvis","")
        query = query.replace("what","")
        query = query.replace("is","")
        query = query.replace("the","")
        date = datetime.datetime.now().strftime("%d %m %y")
        print("Date is : " + str(date))
        eel.DisplayMessage("Date is : " + str(date))
        speak("Today date is " + str(date))

def FindTemperature(query):
        query = query.replace("jarvis","")
        query = query.replace("what","")
        query = query.replace("is","")
        query = query.replace("the","")
        speak("open google cloud")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        # url = f"https://www.google.com/search?q=" + query
        # r = requests.get(url)
        # data = BeautifulSoup(r.text, "html.parser")
        # temp = data.find("div", class_ = "BNeawe").text
        # print(f"The temperature is : {temp}")
        # eel.DisplayMessage(f"The temperature is : {temp}")
        # speak(f"The temperature is {temp}")


def FindWeather(query):
        query = query.replace("jarvis","")
        query = query.replace("what","")
        query = query.replace("is","")
        query = query.replace("the","")
        speak("open google cloud")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        

def OpenYouTube(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        eel.DisplayMessage("Opening YouTube")
        speak("Opening YouTube")
        webbrowser.open(f"youtube.com")

def OpenGoogle(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        eel.DisplayMessage("Opening Google")
        speak("Opening Google")
        webbrowser.open(f"google.com")

def OpenWhatsApp(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        eel.DisplayMessage("Opening")
        speak("Opening...")
        webbrowser.open(f"whatsapp.com")

def OpenBootstrap(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        eel.DisplayMessage("Opening Bootstrap")
        speak("Opening Bootstapp")
        webbrowser.open(f"getbootstrap.com")

def OpenWikipedia(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        eel.DisplayMessage("Opening wikipedia")
        speak("Opening wikipedia")
        webbrowser.open(f"wikipedia.com")

    
def OpenSites(query):
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace(".com","")
        query = query.replace(" ","")
        eel.DisplayMessage("Opening Web")
        speak("Opening web")
        webbrowser.open(f"{query}.com")