import pyttsx3
import speech_recognition


engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1  
        r.energy_threshold = 300  
        audio = r.listen(source, timeout=10 )  
    query=r.recognize_google(audio,language="en-in")

    try:
        print("understanding...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said:{query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query
takeCommand()
if __name__=="__main__":
    while True:
        query=takeCommand()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query=takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir,You can call me anytime")
                    break
                    
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

            
                

    



