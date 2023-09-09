import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():  # This function wishes you when the jarvis is activated
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am jarvis how can i help you!")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-id')
        print(f"user said {query}\n")

    except:
        return "None"
    return query


def Music():  # This function is used to play any music that is on your desktop or from the YouTube
    speak("Tell me the name of the song!")
    musicName = takeCommand()
    pywhatkit.playonyt(musicName)

    speak("Your song has been started! Enjoy Sir")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        # Below are the logics for executing tasks based on query.

        if 'youtube' in query:  # Opens the YouTube on the web browser
            webbrowser.open("youtube.com")

        elif 'how are you' in query:
            speak('I am fine sir!')

        elif 'google' in query:  # Opens google and ask for the topic that you want to search
            speak("Sir! what should i search for you")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'wikipedia' in query:  # Collects the information from the wikipedia website and speaks out the first
            # two sentence from it
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'thank you' in query:
            speak('Your welcome Sir!')

        elif 'rest' in query:  # This is you to terminate our program
            speak("Okay sir going for rest")
            exit()

        elif 'music' in query:
            Music()

        elif 'close the tab' in query:  # This is used to close the tabs from the Google Chrome application
            keyboard.press_and_release('ctrl + w')

        elif 'website' in query:  # This is used to open any kind of website on the web browser
            speak('Which website do you want to browse')
            web1 = takeCommand()
            web2 = 'http://www.' + web1 + '.com'
            webbrowser.open(web2)

        elif 'break' in query:  # This is used to pause a video in YouTube
            keyboard.press_and_release('space bar')

        elif 'play' in query:  # This is used to play a video in YouTube
            keyboard.press_and_release('space bar')

        elif 'full screen' in query:  # This is used to full screen a video in YouTube
            keyboard.press_and_release('f')

        elif 'next' in query:  # This is used to play a video in YouTube
            keyboard.press_and_release('shift + n')

        elif 'backward' in query:  # This is used to backward a video in YouTube for 10 seconds
            keyboard.press_and_release('j')

        elif 'forward' in query:  # This is used to forward a video in YouTube for 10 seconds
            keyboard.press_and_release('l')

        elif 'beginning' in query:  # This is used to start a video in YouTube from the beginning
            keyboard.press_and_release('0')
            speak("Okay sir song started from the beginning")

        elif 'mute' in query:  # This is used to mute a video in YouTube
            keyboard.press_and_release('m')

        elif 'escape full-screen' in query:  # This is used to escape the full screen in YouTube
            keyboard.press_and_release('f')
