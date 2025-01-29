import pyautogui
import time
import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()


def MaximizeWindow(query):
    pyautogui.hotkey('alt','space')
    time.sleep(0.1)
    pyautogui.press('x')

def MinimizeWindow(query):
    pyautogui.hotkey('alt','space')
    time.sleep(0.1)
    pyautogui.press('n')

def CapsLockOn(query):
    pyautogui.press('capslock')

def CapsLockOff(query):
    pyautogui.press('capslock')

def NewTab(query):
    pyautogui.hotkey('ctrl','t')

def NewWindow(query):
    pyautogui.hotkey('ctrl','n')

def IncognitoWindow(query):
    pyautogui.hotkey('ctrl','shift','n')

def HardRefresh(query):
    pyautogui.hotkey('win','ctrl','shift','b')
    time.sleep(0.5)
    speak("System Refreshed")

def OpenHistory(query):
    pyautogui.hotkey('ctrl','h')

def FindOnPage(query):
    pyautogui.hotkey('ctrl','f')

def AllTab(query):
    pyautogui.hotkey('win','tab')

def PressEnterbtn(query):
    pyautogui.press('enter')

def TypeForSearch(query):
    query = query.replace("write","")
    query = query.replace("type","")
    pyautogui.typewrite(query)

def WriteOnSearchBar(query):
    query = query.replace("write","")
    query = query.replace("search","")
    query = query.replace("type","")
    query = query.replace("and","")
    pyautogui.press('/')
    pyautogui.typewrite(query)
    speak("Searching")
    time.sleep(0.5)
    pyautogui.press('enter')
