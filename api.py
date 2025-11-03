import requests
import pyttsx3
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


api_key = "c04cda1405e44a61808223519250606"  # Replace with your actual API key
base_url = "http://api.weatherapi.com/v1"

def fetch_weather(city_name):
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"
    response = requests.get(complete_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather_info(weather_data):
    if weather_data:
        location = weather_data["location"]["name"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        speak(f"Weather in {location},sir")
        speak(f"Temperature is {temperature}°C,sir")
        speak(f"Condition is {condition},sir")
    else:
        speak("Error retrieving weather data.")


indian_cities = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai",
    "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal",
    "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra"
    ]    


api_key="Bearer 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"




                    


    



