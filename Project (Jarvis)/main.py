import speech_recognition as sr
import webbrowser 
import pyttsx3
import music_lib
import requests
import sys

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "66dba4d8a88e414cb88d154572cb134d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    # Opening links

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facbook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

        # Playing Music

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] #Splits the converted list for obtaining the sone name
        link = music_lib.music[song]
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry i can't find the song ")

        # Fetching News from API

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parsing the JSON response
            data = r.json()
            #extracting the articles
            articles = data.get('articles',[])
            #taking headlines
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry i cannot fetch the news today")

    # Exiting jarvis

    elif "exit" in c.lower() or "goodbye" in c.lower():
        speak("Goodbye, Sir!")
        sys.exit()  # Exits the program
        
if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        #Listening for the waking word Jarvis...
        #obtaining audio from the mic...

        r = sr.Recognizer()

        #recognize speech using Recognize_google
        print("Recognizing...")
        try:
            with sr.Microphone() as source: 
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("Yess Sir")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error!".format(e))

