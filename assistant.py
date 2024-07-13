import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes
import pyaudio

engine = pyttsx3.init() #initializaiton of TEXT TO SPEECH LIBIRARY pyttsx3

#function to speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#functiont to speak time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

#functon to speak date
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

#function for INITIAL GREETINGS!
def wishme():
    print("Welcome back , How are you ? Hope you ar well!!")
    speak("Welcome back , How are you ? Hope you ar well!!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif 12 <= hour < 16:
        speak("Good Afternoon !!")
        print("Good Afternoon !!")
    elif 16 <= hour < 21:
        speak("Good Evening !!")
        print("Good Evening !!")
    elif 21<= hour <24 :
        speak('Its time to sleep but still Good Evening!!')
        print('Its time to sleep but still Good Evening!!')
    else:
        speak("Good Night Sir, It's time to sleep , If you do not have any Query then See You Tommorrow !")

    speak("KK at your service , please tell me how may I help you.")
    print("KK at your service , please tell me how may I help you.")

#function to take screenshot
def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("JARVIS/jarvis.jpg")
    img.save(img_path)

#function to take command from user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    speak("I am KK created by Mr.Kamat and I'm a desktop voice assistant")
    print("I am KK created by Mr.Kamat and I'm a desktop voice assistant")
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm KK created by Mr. Kamat and I'm a desktop voice assistant.")
            print("I'm KK created by Mr. Kamat and I'm a desktop voice assistant.")

        elif "you" in query:
            speak("I'm fine too , What about you?")
            print("I'm fine too, What about you?")

        elif "fine" in query:
            speak("Glad to hear that !!")
            print("Glad to hear that !!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
        
        elif "all well" in query:
            speak("Good to see it !")
            print("Good to see it !")
            
        elif "wikipedia" in query:
            try:
                speak("Okkk ! Please wait while I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please try for something else")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")
        
        elif "open facebook" in query:
            wb.open("facebook.com")
        
        elif "open instagram" in query:
            wb.open("https://www.instagram.com/")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir) #lists all the files in the
            print(songs)
            x = len(songs)
            y = random.randint(0, x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        
        elif "chat gpt" in query:
            speak("Ok sir, please wait while I'm opening chat gpt")
            wb.open("https://chat.openai.com/chat")

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            
        elif "joke" in query:
            joke_1 = pyjokes.get_joke(language='en',category='neutral')
            print(joke_1)
            speak("Here is you joke to lift your mood")
            speak(joke_1)
            print(joke_1)
            speak('hahahahahahhh')

        elif "offline" in query:
            quit()
