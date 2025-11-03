import speech_recognition as sr
import os
import subprocess

# Define commands for opening and closing apps
app_commands = {
    "open notepad": lambda: subprocess.Popen("notepad.exe"),
    "close notepad": lambda: os.system("taskkill /IM notepad.exe /F"),
    
    "open calculator": lambda: subprocess.Popen("calc.exe"),
    "close calculator": lambda: os.system("taskkill /IM calculator.exe /F"),
    
    "open chrome": lambda: subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
    "close chrome": lambda: os.system("taskkill /IM chrome.exe /F"),
    
    "open edge": lambda: subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"),
    "close edge": lambda: os.system("taskkill /IM msedge.exe /F"),
    
    "open file explorer": lambda: subprocess.Popen("explorer.exe"),
    "close file explorer": lambda: os.system("taskkill /IM explorer.exe /F"),
    
    "open command prompt": lambda: subprocess.Popen("cmd.exe"),
    "close command prompt": lambda: os.system("taskkill /IM cmd.exe /F"),
    
    "open paint": lambda: subprocess.Popen("mspaint.exe"),
    "close paint": lambda: os.system("taskkill /IM mspaint.exe /F"),
    
    "open vlc": lambda: subprocess.Popen("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"),
    "close vlc": lambda: os.system("taskkill /IM vlc.exe /F"),
    
    "open word": lambda: subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"),
    "close word": lambda: os.system("taskkill /IM WINWORD.EXE /F"),
    
    "open excel": lambda: subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"),
    "close excel": lambda: os.system("taskkill /IM EXCEL.EXE /F"),
    
    "open powerpoint": lambda: subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"),
    "close powerpoint": lambda: os.system("taskkill /IM POWERPNT.EXE /F"),
    
    "open outlook": lambda: subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"),
    "close outlook": lambda: os.system("taskkill /IM OUTLOOK.EXE /F"),
    
    "open spotify": lambda: subprocess.Popen("C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe"),
    "close spotify": lambda: os.system("taskkill /IM Spotify.exe /F"),
    
    "open steam": lambda: subprocess.Popen("C:\\Program Files (x86)\\Steam\\steam.exe"),
    "close steam": lambda: os.system("taskkill /IM steam.exe /F"),
    
    "open adobe reader": lambda: subprocess.Popen("C:\\Program Files\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"),
    "close adobe reader": lambda: os.system("taskkill /IM AcroRd32.exe /F"),
    
    "open task manager": lambda: subprocess.Popen("taskmgr.exe"),
    "close task manager": lambda: os.system("taskkill /IM taskmgr.exe /F"),
    
    "open settings": lambda: subprocess.Popen("ms-settings:"),
    
    "open control panel": lambda: subprocess.Popen("control.exe"),
}

def listen_for_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)



