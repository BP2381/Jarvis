import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

jarvis = "jarvis"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return "None"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return "None"
    except sr.RequestError:
        print("Network error.")
        return "None"
    return query

def searchGoogle(query):
    if "google" in query:
        query = query.replace("google", "")
        query = query.replace("open ", "")
        query = query.replace(jarvis, "")
        query = query.replace("search", "")
        speak("This is what I found on Google.")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, 1)
            speak(result)
        except:
            speak("No speakable result found.")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search.")
        query = query.replace("open youtube and search", "")
        query = query.replace("open youtube and", "")
        query = query.replace(jarvis, "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("open ", "")
        query = query.replace("search", "")
        query = query.replace(jarvis, "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        except:
            speak("Sorry, no Wikipedia result found.")
