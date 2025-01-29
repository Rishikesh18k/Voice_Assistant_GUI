import pyttsx3
import speech_recognition
import time
import pyautogui
import psutil       # pip install psutill
import winshell     # pip install winshell
import requests
import os
import eel

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.")
        return ""
    return query

def ShutDown(query):
    query = query.replace("jarvis","")
    eel.DisplayMessage("Make sure All of your applicatios are closed")
    speak("Make sure All of your applicatios are closed")
    os.system("shutdown /s /t 2")

def Restart(query):
    query = query.replace("jarvis","")  
    os.system("shutdown /r /t 2")

def SystemWork(query):
    # if f"Screenshot".lower() in query.lower():
        print("Please tell me the file name")
        eel.DisplayMessage("Please tell me the file name.")
        speak("Please tell me the file name")
        name = takeCommand().lower()
        eel.DisplayMessage("please hold the screen")
        speak("please hold the screen")
        time.sleep(1)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        eel.DisplayMessage("Screenshot Captured")
        speak("Screenshot Captured")
        print("Screenshot Captured")

def CPUstatus(query):
        usage = str(psutil.cpu_percent())
        print("CPU is at : " +  usage +"%")
        eel.DisplayMessage("CPU is at : " +  usage +"%")
        speak("CPU is at " + usage +" Percent")
        battery = str(psutil.sensors_battery())
        print("Battery at : " + battery)
        eel.DisplayMessage("Battery at : " + battery)
        speak(battery) 

def Recyclebin(query):
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        eel.DisplayMessage("OK, Recycle bin Recycled")
        speak("OK, Recycle bin Recycled")

def IPaddress(query):
    if f"ip".lower() in query.lower():
        try:
            ipadd = requests.get('https://api.ipify.org').text
            speak("please wait, Checking Your IP address")
            print("Your IP address is : " + ipadd)
            eel.DisplayMessage("Your IP address is : " + ipadd)
            speak("Your IP address is " + ipadd)
        except Exception as e:
            print("Network is Weak, please try again some time latter")
            eel.DisplayMessage("Network is Weak, please try again some time latter")
            speak("Network is Weak, please try again some time latter")

def VolumeUp(query):
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

def VolumeDown(query): 
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

def VolumeMute(query):
        pyautogui.press("volumemute")
def VolumeUnMute(query):
        pyautogui.press("volumemute")

def OpenCamera(query):
    query = query.replace("open","")
    query = query.replace("jarvis","")
    eel.DisplayMessage("Opening Camera")
    speak("Opening Camera")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.typewrite("camera")
    pyautogui.press("enter")

def OpenSystem(query):
    query = query.replace("open","")
    query = query.replace("jarvis","")
    eel.DisplayMessage("Opening System")
    speak("Opening System")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.typewrite("about system")
    pyautogui.press("enter")

def OpenSetting(query):
    query = query.replace("open","")
    query = query.replace("jarvis","")
    eel.DisplayMessage("Opening Setting")
    speak("Opening Settings")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.typewrite("setting")
    pyautogui.press("enter")

def OpenTaskManager(query):
    eel.DisplayMessage("Opening Task Manager")
    speak("Opening Task Manager")
    pyautogui.hotkey("ctrl","shift","esc")