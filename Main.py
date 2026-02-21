import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import subprocess
import MusicLibrary
import requests
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)
newsapi = "4c437c5834824f63abb401700ad92cba"
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def speak(text):
    text = text.strip()
    subprocess.run(["say", text])
    time.sleep(0.5)

'''def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)'''#pyttsx3 use for window for best result but for mac use import os for best result

def ai_process(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are Jarvis, a virtual assistant. "
                "1. Detect the language style of the user's message. "
                "2. If the message is in Gujarati, reply in Gujarati. "
                "3. If the message is in English, reply in English. "
                "5. If the message is in Hindi, reply in Hindi. "
                "5. Keep the tone natural, friendly, and human-like."
                "Always answer in 3 to 4 lines only.\n\n"
                + user_input
            )
        )
        return response.text

    except Exception as e:
        return f"Jarvis Error:{e}"

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in  c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles' , [])

            #Print the headline
            for article in articles:
                speak(article['title'])
    
    else:
        # let Gemini handle the request
        output = ai_process(c)
        speak(output)

if __name__ == "__main__":
    speak("Jarvis is listen now...")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from microphoe
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word= r.recognize_google(audio)
            if(word.lower() == "Jarvis"):
                speak("Yaa")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    ProcessCommand(command)
        except Exception  as e:
            print("Error:",e)   
