# This is a sample Python script.
import webbrowser
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import speech_recognition as sr
import pyttsx3
from speech_recognition.__main__ import source

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Function to speak text
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Function to listen to user's voice
def listen():
    with sr.Microphone() as source:
        print("boleye sir......")
        speak("good afternoon babu bahi how i can hekp you")
        audio = recognizer.listen(source, timeout=5)
        try:
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""

# Main loop
while True:
    user_input = listen()
    if user_input:
        print("You said:", user_input)
        if "hello jarvis" in user_input:
            speak("yes sir.... i am happy to talk with u")
        elif "bye" in user_input:
            speak("bye sir nice to meet u and call me agin!")
            break
        elif "how are you" in user_input:
            speak("main thik hu aap kise ho g!")
            break
        elif "what is your name" in user_input:
            speak("my name is jarvish sir")
            break
        elif "jarvis who made you" in user_input:
            speak("zakki sir made me !")
            break
        elif "open chatgpt" in user_input:
            speak("sorry i can't!")
            break
        elif "i love u" in user_input:
            speak("sala kamina!  i am assistant not human")
            break
        elif "jarvis open youtube" in user_input:
            webbrowser.open("https://youtube.com")
            speak("opening youtube sir....")
            break
        elif "open google" in user_input:
            webbrowser.open("https://google.com")
            speak("opening google sir....")
            break
        elif "open portal" in user_input:
            webbrowser.open("http://103.114.208.150/elearning")
            speak("opening portel sir....")
            break
        elif "open gfg" in user_input:
            webbrowser.open("https://www.bing.com/ck/a?!&&p=0f4b4f19877f9fb2JmltdHM9MTY5NTQyNzIwMCZpZ3VpZD0wZTBkN2M3ZC04M2JkLTYyYWMtM2I1Mi02ZDQ4ODIwZjYzNWMmaW5zaWQ9NTIyMg&ptn=3&hsh=3&fclid=0e0d7c7d-83bd-62ac-3b52-6d48820f635c&psq=gfg&u=a1aHR0cHM6Ly9wcmFjdGljZS5nZWVrc2ZvcmdlZWtzLm9yZy9wcm9ibGVtLW9mLXRoZS1kYXk&ntb=1")
            speak("opening gfg sir....")
            break
        elif "open java" in user_input:
            webbrowser.open("https://www.bing.com/ck/a?!&&p=9b49e4900f5436b7JmltdHM9MTY5NTQyNzIwMCZpZ3VpZD0wZTBkN2M3ZC04M2JkLTYyYWMtM2I1Mi02ZDQ4ODIwZjYzNWMmaW5zaWQ9NTIxOA&ptn=3&hsh=3&fclid=0e0d7c7d-83bd-62ac-3b52-6d48820f635c&psq=java+online+compiler&u=a1aHR0cHM6Ly93d3cucHJvZ3JhbWl6LmNvbS9qYXZhLXByb2dyYW1taW5nL29ubGluZS1jb21waWxlci8&ntb=1")
            speak("opening java sir....")
            break
        elif "i love u" in user_input:
            speak("sala kamina!  i am assistant not human")
            break
        elif "who is my brother" in user_input:
            speak("zeeshan")
            break
        elif "jarvis who is my uncle" in user_input:
            speak("babu bahi")
            break


        else:
            speak("I didn't understand that. Please repeat.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
