import pyttsx3
import speech_recognition
import pyautogui
import datetime
import requests
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, timeout=4)
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except speech_recognition.WaitTimeoutError:
        print("Listening timed out while waiting for phrase.")
        return "None"
    except speech_recognition.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return "None"
    except speech_recognition.RequestError:
        print("Network error.")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break



                elif "open" in query or "close" in query:
                    from apps import app_commands
                    if query in app_commands:
                        app_commands[query]()
                    else:
                        query=query.replace("open","")
                        query=query.replace("jarvis","")
                        query=query.replace("the","")
                        query=query.replace(" ","")
                        pyautogui.press("super")
                        pyautogui.sleep(2)
                        pyautogui.typewrite(query)
                        pyautogui.press("enter")
                        speak(f"opening {query},sir")



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                
                elif "play" in query:
                    pyautogui.press("K")
                    speak("video played")
                
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboad import volumeup
                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboad import volumedown
                    speak("Turning volume down,sir")
                    volumedown()

                elif "scroll up" in query:
                    from pynput.mouse import Controller
                    mouse=Controller()
                    mouse.scroll(0, 6)
                    speak("scrolling up,sir")
                
                elif "the time" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir,the time is {strtime}")
                
                elif "weather" in query:
                    from api import fetch_weather
                    from api import display_weather_info
                    from api import indian_cities
                    for indian_cities in query:
                        city_name=indian_cities
                    else:
                        city_name="Hyderabad"
                    fetch_weather(city_name)
                    weather_data = fetch_weather(city_name)
                    display_weather_info(weather_data)

                else:
                    response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": "",  # Replace with your key
                        "Content-Type": "application/json",
                      },
                    data=json.dumps({
                        "model": "meta-llama/llama-3.3-70b-instruct:free",
                        "messages": [{"role": "an ai assistant which is freindly and give two  line answers in effective way", "content": f"{query}" }]
                    })
                    )
                 # Process API response and speak the result
                    response_data = response.json()
                    response_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response.")
                    speak(response_text)

                
                
