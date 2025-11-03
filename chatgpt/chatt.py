import pyttsx3
import speech_recognition
import requests
import json

engine = pyttsx3.init("sapi5")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as source:
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, timeout=4)
        return r.recognize_google(audio, language="en-in")
    except:
        return "None"

def process_query(query):
    if "time" in query:
        import datetime
        return f"The time is {datetime.datetime.now().strftime('%H:%M')}"

    elif "weather" in query:
        return "Currently cloudy in Hyderabad, 28°C."  # Replace with your API

    else:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Your API KEY####################",  # Replace with key
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "meta-llama/llama-3.3-70b-instruct:free",
                    "messages": [{"role": "user", "content": query}]
                })
            )
            response_data = response.json()
            return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response.")
        except:
            return "Failed to connect to assistant."
