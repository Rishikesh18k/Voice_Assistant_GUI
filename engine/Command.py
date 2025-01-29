import pyttsx3
import speech_recognition    # pip install SpeechRecognition
import eel
import time 

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
    except Exception as e:
        print(e)
        print("Say that again please.")
        eel.DisplayMessage("Say that again please.")
        time.sleep(2)
        return ""
    return query

@eel.expose
def AllCommand():
    # while True:
        query = takeCommand().lower()
        if f"Hello".lower() in query.lower():
            from engine.ChatWithJarvis import ChatA
            ChatA(query)
        elif f"hii".lower() in query.lower():
            from engine.ChatWithJarvis import ChatA
            ChatA(query)
        elif f"Jarvis".lower() in query.lower():
            from engine.ChatWithJarvis import ChatA
            ChatA(query)
        elif f"How r u".lower() in query.lower():
            from engine.ChatWithJarvis import ChatB
            ChatB(query)
        elif f"How about you".lower() in query.lower():
            from engine.ChatWithJarvis import ChatB
            ChatB(query)
        elif f"How about u".lower() in query.lower():
            from engine.ChatWithJarvis import ChatB
            ChatB(query)
        elif f"How are you".lower() in query.lower():
            from engine.ChatWithJarvis import ChatB
            ChatB(query)
        elif f"i am fine".lower() in query.lower():
            from engine.ChatWithJarvis import ChatC
            ChatC(query)
        elif f"i m fine".lower() in query.lower():
            from engine.ChatWithJarvis import ChatC
            ChatC(query)
        elif f"what are you doing".lower() in query.lower():
            from engine.ChatWithJarvis import ChatD
            ChatD(query)
        elif f"what r u doing".lower() in query.lower():
            from engine.ChatWithJarvis import ChatD
            ChatD(query)
        elif f"who are you".lower() in query.lower():
            from engine.ChatWithJarvis import ChatE
            ChatE(query)
        elif f"hu r u".lower() in query.lower():
            from engine.ChatWithJarvis import ChatE
            ChatE(query)
        elif f"who are created you".lower() in query.lower():
            from engine.ChatWithJarvis import ChatF
            ChatF(query)
        elif f"hu r created u".lower() in query.lower():
            from engine.ChatWithJarvis import ChatF
            ChatF(query)
        elif f"I am very happy".lower() in query.lower():
            from engine.ChatWithJarvis import ChatG
            ChatG(query)
        elif f"I am happy".lower() in query.lower():
            from engine.ChatWithJarvis import ChatG
            ChatG(query)
        

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (((Open Function))) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        elif f"visual studio code".lower() in query.lower():
            from engine.OpenMSapp import OpenVsCode
            OpenVsCode(query)
        elif f"vs  code".lower() in query.lower():
            from engine.OpenMSapp import OpenVsCode
            OpenVsCode(query)
        elif f"open control panel".lower() in query.lower():
            from engine.OpenMSapp import OpenControlPanel
            OpenControlPanel(query)
        elif f"open paint".lower() in query.lower():
            from engine.OpenMSapp import OpenPaint
            OpenPaint(query)
        elif f"open One Note".lower() in query.lower():
            from engine.OpenMSapp import OpenOneNote    
            OpenOneNote(query)
        elif f"open Gmail".lower() in query.lower():
            from engine.OpenMSapp import OpenGamil
            OpenGamil(query)
        elif f"camera".lower() in query.lower():
            from engine.SystemCall import OpenCamera
            OpenCamera(query)
        elif f"Task manager".lower() in query.lower():
            from engine.SystemCall import OpenTaskManager
            OpenTaskManager(query)
        elif f"open Setting".lower() in query.lower():
            from engine.SystemCall import OpenSetting
            OpenSetting(query)
        elif f"About System".lower() in query.lower():
            from engine.SystemCall import OpenSystem
            OpenSystem(query)
        elif f"About PC".lower() in query.lower():
            from engine.SystemCall import OpenSystem
            OpenSystem(query)
        elif f"open word".lower() in query.lower():
            from engine.OpenMSapp import OpenMSworld
            OpenMSworld(query)
        elif f"open PowerPoint".lower() in query.lower():
            from engine.OpenMSapp import OpenPowerpoint
            OpenPowerpoint(query)
        elif f"open notepad".lower() in query.lower():
            from engine.OpenMSapp import OpenNotepad
            OpenNotepad(query)
        elif f"open excel".lower() in query.lower():
            from engine.OpenMSapp import OpenExcel
            OpenExcel(query)
        elif f"open command prompt".lower() in query.lower():
            from engine.OpenMSapp import OpenCommandPrompt
            OpenCommandPrompt(query)
        elif f"open cmd".lower() in query.lower():
            from engine.OpenMSapp import OpenCommandPrompt
            OpenCommandPrompt(query)
        elif f"open terminal".lower() in query.lower():
            from engine.OpenMSapp import OpenTerminal
            OpenTerminal(query)
        elif f"open powershell".lower() in query.lower():
            from engine.OpenMSapp import OpenTerminal
            OpenTerminal(query)
        elif f"open Google Chrome".lower() in query.lower():
            from engine.OpenMSapp import OpenChrome
            OpenChrome(query)
        elif f"open YouTube".lower() in query.lower():
            from engine.SearchNow import OpenYouTube
            OpenYouTube(query)
        elif f"open Google".lower() in query.lower():
            from engine.SearchNow import OpenGoogle
            OpenGoogle(query)
        elif f"open whatsapp".lower() in query.lower():
            from engine.SearchNow import OpenWhatsApp
            OpenWhatsApp(query)
        elif f"open bootstrap".lower() in query.lower():
            from engine.SearchNow import OpenBootstrap
            OpenBootstrap(query)
        elif f"open wikipedia".lower() in query.lower():
            from engine.SearchNow import OpenWikipedia
            OpenWikipedia(query)
        elif f"location".lower() in query.lower():
            from engine.SearchNow import SearchLocation
            SearchLocation(query)
        elif f"map".lower() in query.lower():
            from engine.SearchNow import SearchLocation
            SearchLocation(query)
  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (((Shrtcut Key Function))) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        elif f"caps lock on".lower() in query.lower():
            from engine.ShortcutKey import CapsLockOn
            CapsLockOn(query)
        elif f"caps lock off".lower() in query.lower():
            from engine.ShortcutKey import CapsLockOff
            CapsLockOff(query)
        elif f"maximize".lower() in query.lower():
            from engine.ShortcutKey import MaximizeWindow
            MaximizeWindow(query)
        elif f"minimise".lower() in query.lower():
            from engine.ShortcutKey import MinimizeWindow
            MinimizeWindow(query)
        elif f"new tab".lower() in query.lower():
            from engine.ShortcutKey import NewTab
            NewTab(query)
        elif f"new window".lower() in query.lower():
            from engine.ShortcutKey import NewWindow
            NewWindow(query)
        elif f"open history".lower() in query.lower():
            from engine.ShortcutKey import OpenHistory
            OpenHistory(query)
        elif f"open incognito window".lower() in query.lower():
            from engine.ShortcutKey import IncognitoWindow
            IncognitoWindow(query)
        elif f"Find".lower() in query.lower():
            from engine.ShortcutKey import FindOnPage
            FindOnPage(query)
        elif f"search".lower() in query.lower():
            from engine.ShortcutKey import WriteOnSearchBar
            WriteOnSearchBar(query) 
        elif f"hard refresh".lower() in query.lower():
            from engine.ShortcutKey import HardRefresh
            HardRefresh(query)
        elif f"open all tab".lower() in query.lower():
            from engine.ShortcutKey import AllTab
            AllTab(query)
        elif f"enter".lower() in query.lower():
            from engine.ShortcutKey import PressEnterbtn
            PressEnterbtn(query)
        elif f"type".lower() in query.lower():
            from engine.ShortcutKey import TypeForSearch
            TypeForSearch(query)
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (((Search Function))) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        elif f"on YouTube".lower() in query.lower():
            from engine.SearchNow import SearchOnYouTube
            SearchOnYouTube(query)
        elif f"on Google".lower() in query.lower():
            from engine.SearchNow import SearchOnGoogle
            SearchOnGoogle(query)
        elif f"According to google".lower() in query.lower():
            from engine.SearchNow import SearchOnGoogle
            SearchOnGoogle(query)
        elif f"wikipedia".lower() in query.lower():
            from engine.SearchNow import SearchOnWikipedia
            SearchOnWikipedia(query)
        elif f"about".lower() in query.lower():
            from engine.SearchNow import SearchOnWikipedia
            SearchOnWikipedia(query)  
        elif f"Video".lower() in query.lower():
            from engine.SearchNow import SearchVideo
            SearchVideo(query)
        elif f"Photo".lower() in query.lower():
            from engine.SearchNow import SearchPhoto
            SearchPhoto(query)
        elif f"Game".lower() in query.lower():
            from engine.SearchNow import SearchGame
            SearchGame(query)
        elif f"picture".lower() in query.lower():
            from engine.SearchNow import SearchPhoto
            SearchPhoto(query)
        elif f"Pic".lower() in query.lower():
            from engine.SearchNow import SearchPhoto
            SearchPhoto(query)
        elif f"image".lower() in query.lower():
            from engine.SearchNow import SearchPhoto
            SearchPhoto(query)
        elif f"wallpaper".lower() in query.lower():
            from engine.SearchNow import SearchWallpaper
            SearchWallpaper(query)
        elif f"Song".lower() in query.lower():
            from engine.SearchNow import SearchMusic
            SearchMusic(query)
        elif f"music".lower() in query.lower():
            from engine.SearchNow import SearchMusic
            SearchMusic(query)
        elif f"time".lower() in query.lower():
            from engine.SearchNow import Time
            Time(query)
        elif f"date".lower() in query.lower():
            from engine.SearchNow import FindDate
            FindDate(query)
        elif f"Temperature".lower() in query.lower():
            from engine.SearchNow import FindTemperature
            FindTemperature(query)
        elif f"weather".lower() in query.lower():
            from engine.SearchNow import FindWeather
            FindWeather(query)
        elif f"shut down".lower() in query.lower():
            from engine.SystemCall import ShutDown
            ShutDown(query)
        elif f"Restart".lower() in query.lower():
            from engine.SystemCall import Restart
            Restart(query)
        elif f"Screenshot".lower() in query.lower():
            from engine.SystemCall import SystemWork
            SystemWork(query)
        elif f"CPU status".lower() in query.lower():
            from engine.SystemCall import CPUstatus
            CPUstatus(query) 
        elif f"recycle bin".lower() in query.lower():
            from engine.SystemCall import Recyclebin
            Recyclebin(query)
        elif f"ip".lower() in query.lower():
            from engine.SystemCall import IPaddress
            IPaddress(query)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (((Close Function))) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        elif f"close chrome".lower() in query.lower():
            from engine.CloseApp import CloseChrome
            CloseChrome(query)
        elif f"close google chrome".lower() in query.lower():
            from engine.CloseApp import CloseChrome
            CloseChrome(query)  
        elif f"close microshoft".lower() in query.lower():
            from engine.CloseApp import CloseBroswer
            CloseBroswer(query)
        elif f"close microshoft edge".lower() in query.lower():
            from engine.CloseApp import CloseBroswer
            CloseBroswer(query)
        elif f"close ms edge".lower() in query.lower():
            from engine.CloseApp import CloseBroswer
            CloseBroswer(query)
        elif f"close Notepad".lower() in query.lower():
            from engine.CloseApp import CloseNotepad
            CloseNotepad(query)
        elif f"close Visual Studio Code".lower() in query.lower():
            from engine.CloseApp import CloseVsCode
            CloseVsCode(query)
        elif f"close vs Code".lower() in query.lower():
            from engine.CloseApp import CloseVsCode
            CloseVsCode(query)
        elif f"close Word".lower() in query.lower():
            from engine.CloseApp import CloseWord
            CloseWord(query)
        elif f"close PowerPoint".lower() in query.lower():
            from engine.CloseApp import ClosePowerPoint
            ClosePowerPoint(query)
        elif f"close excel".lower() in query.lower():
            from engine.CloseApp import CloseExcel
            CloseExcel(query)
        elif f"close command prompt".lower() in query.lower():
            from engine.CloseApp import CloseCommandPrompt
            CloseCommandPrompt(query)
        elif f"close cmd".lower() in query.lower():
            from engine.CloseApp import CloseCommandPrompt
            CloseCommandPrompt(query)
        elif f"close terminal".lower() in query.lower():
            from engine.CloseApp import CloseTerminal
            CloseTerminal(query)
        elif f"close powershell".lower() in query.lower():
            from engine.CloseApp import CloseTerminal
            CloseTerminal(query)
        elif f"Volume up".lower() in query.lower():
            from engine.SystemCall import VolumeUp
            VolumeUp(query)
        elif f"Volume down".lower() in query.lower():
            from engine.SystemCall import VolumeDown
            VolumeDown(query)
        elif f"Volume mute".lower() in query.lower():
            from engine.SystemCall import VolumeMute
            VolumeMute(query)
        elif f"Volume unmute".lower() in query.lower():
            from engine.SystemCall import VolumeUnMute
            VolumeUnMute(query)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif f"open".lower() in query.lower():
            from engine.SearchNow import OpenSites
            OpenSites(query)
        eel.ShowIndex()