import pyttsx3    # pip install pyttsx3
import eel

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def ChatA(query):
    print("Hi, How can I help You")
    eel.DisplayMessage("Hi, How can I help you")
    speak("Hi, How can I help You")

def ChatB(query):
    print("I am Great, thank you for asking! How About you?")
    eel.DisplayMessage("I am Great, thank you for asking! How about you?")
    speak("I am Great, thank you for asking!  How about you?")

def ChatC(query):
    print("Awesome!")
    eel.DisplayMessage("Awesome!")
    speak("Awesome!")

def ChatD(query):
    print("Sorry, I didn't Understand.")
    eel.DisplayMessage("Sorry, I didn't Understand.")
    speak("Sorry, I didnot Understand")

def ChatE(query):
    print("I am jarvis assistan. How can I help you?")
    eel.DisplayMessage("I am jarvis assistan. How can I help you?")
    speak("I am jarvis assistan. How can I help you?")

def ChatF(query):
    print("A first I was just an idea and Now here I am")
    eel.DisplayMessage("A first I was just an idea and Now here I am")
    speak("A first I was just an idea and Now here I am")

def ChatG(query):
    print("I'm happy you're happy")
    eel.DisplayMessage("I'm happy you're happy")
    speak("I'm happy you're happy")