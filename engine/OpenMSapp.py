import pyttsx3
import os
import pyautogui    # pip install pyautogui
import time
import eel

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def OpenNotepad(query):
    print("Opening Notepad")
    eel.DisplayMessage("Opening Notepad")
    speak("Opening Notepad")
    pyautogui.press("win")
    time.sleep(0.1)
    pyautogui.write("Notepad")
    time.sleep(0.2)
    pyautogui.press("enter")


def OpenPowerpoint(query):
    eel.DisplayMessage("Opening PowerPoint")
    speak("Opening PowerPoint")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("PowerPoint")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenExcel(query):
    eel.DisplayMessage("Opening Excel")
    speak("Opening Excel")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Excel")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenMSworld(query):
    eel.DisplayMessage("Opening Micrshoft Word")
    speak("Opening Micrshoft Word")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Word")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenChrome(query):
    eel.DisplayMessage("Opening Google Chrome")
    speak("Opening Google Chrome")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Google Chrome")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenVsCode(query):
    eel.DisplayMessage("Opening VS-Code")
    speak("Opening...")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Visual Studio Code")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenControlPanel(query):
    eel.DisplayMessage("Opening Control Panel")
    speak("Opening...")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Control Panel")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenPaint(query):
    eel.DisplayMessage("Opening Paint")
    speak("Opening...")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Paint")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenOneNote(query):
    eel.DisplayMessage("Opening OneNote")
    speak("Opening...")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("OneNote")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenGamil(query):
    eel.DisplayMessage("Opening Gmail")
    speak("Opening...")
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.write("Gmail")
    time.sleep(0.2)
    pyautogui.press("enter")

def OpenCommandPrompt(query):
    eel.DisplayMessage("Opening Command Prompt")
    speak("Opening...")
    os.system("start cmd")

def OpenTerminal(query):
    eel.DisplayMessage("Opening Window PowerShell")
    speak("Opening...")
    os.system("start powershell")

