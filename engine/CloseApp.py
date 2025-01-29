import os
import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def CloseChrome(query):
        speak("Closing...")
        os.system("taskkill /f /im chrome.exe")

def CloseBroswer(query):
        speak("Closing...")
        os.system("taskkill /f /im msedge.exe")
def CloseNotepad(query):
        speak("Closing...")
        os.system("taskkill /f /im notepad.exe")

def CloseWord(query):
        speak("Closing...")
        os.system("taskkill /f /im WINWORD.EXE")

def ClosePowerPoint(query):
        speak("Closing...")
        os.system("taskkill /f /im POWERPNT.EXE")

def CloseExcel(query):
        speak("Closing...")
        os.system("taskkill /f /im EXCEL.EXE")

def CloseVsCode(query):
        speak("Closing...")
        os.system("taskkill /f /im vscode.exe")


def CloseCommandPrompt(query):
        speak("Closing...")
        os.system("taskkill /f /im cmd.exe")

def CloseTerminal(query):
        speak("Closing...")
        os.system("taskkill /f /im powershell.exe")
