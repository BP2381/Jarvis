import pyttsx3
import speech_recognition
import pyautogui
import datetime
import requests
import json
import tkinter as tk
import threading

# Hide main Tkinter root window
root = tk.Tk()
root.withdraw()

# Text-to-speech setup
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ✅ Fixed VoicePulse class
class VoicePulse:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Jarvis Listening...")
        self.root.geometry("300x300")
        self.root.configure(bg='black')
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='black', highlightthickness=0)
        self.canvas.pack()
        self.pulse = self.canvas.create_oval(100, 100, 200, 200, fill="cyan", outline="white")
        self.running = True
        self.animate_thread = threading.Thread(target=self.animate, daemon=True)
        self.animate_thread.start()

    def animate(self):
        grow = True
        size = 50
        while self.running:
            if grow:
                size += 2
                if size >= 100:
                    grow = False
            else:
                size -= 2
                if size <= 50:
                    grow = True
            self.canvas.coords(self.pulse, 150 - size, 150 - size, 150 + size, 150 + size)
            self.canvas.update()
            self.canvas.after(50)

    def stop(self):
        self.running = False
        self.root.destroy()

def takeCommand():
    pulse = VoicePulse()
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
        print("Listening timed out.")
        pulse.stop()
        return "None"
    except speech_recognition.UnknownValueError:
        print("Didn't understand.")
        pulse.stop()
        return "None"
    except speech_recognition.RequestError:
        print("Network error.")
        pulse.stop()
        return "None"
    pulse.stop()
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
                        query = query.replace("open", "").replace("jarvis", "").replace("the", "").replace(" ", "")
                        pyautogui.press("super")
                        pyautogui.sleep(2)
                        pyautogui.typewrite(query)
                        pyautogui.press("enter")
                        speak(f"Opening {query}, sir")

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
                    speak("Video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "volume up" in query:
                    from keyboad import volumeup
                    speak("Turning volume up, sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboad import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "scroll up" in query:
                    from pynput.mouse import Controller
                    mouse = Controller()
                    mouse.scroll(0, 6)
                    speak("Scrolling up, sir")

                elif "the time" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strtime}")

                elif "weather" in query:
                    from api import fetch_weather, display_weather_info
                    city_name = "Hyderabad"
                    weather_data = fetch_weather(city_name)
                    display_weather_info(weather_data)

                else:
                    response = requests.post(
                        url="https://openrouter.ai/api/v1/chat/completions",
                        headers={
                            "Authorization": "Bearer sk-or-v1-17fe909009ab8fa37017b430f8ad674fcc62a9b18f7239d5ed48a24ca2aefb2",  # 🔐 Add your API key here
                            "Content-Type": "application/json",
                        },
                        data=json.dumps({
                            "model": "meta-llama/llama-3.3-70b-instruct:free",
                            "messages": [
                                {"role": "an ai assistant which is friendly and give two line answers in effective way", "content": f"{query}"}
                            ]
                        })
                    )
                    response_data = response.json()
                    response_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response.")
                    speak(response_text)