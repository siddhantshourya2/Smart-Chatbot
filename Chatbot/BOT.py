import pyttsx3                            
import speech_recognition as sr           
import datetime
import wikipedia                          
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("I am Rica. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'do nothing' in query:
          exit
        
        elif "hello" in query:
            speak("hi")
            
        elif "how are you" in query:
            speak("I am fine thank you")
            
        elif "what is your name" in query:
            speak("Everyone knows me with my name Rica")
            
        elif "Who made you?" in query:
            speak("I am made by the team Six Sense")
            
        elif "Who is you leader" in query:
            speak("My leader name is Siddhant")

        elif "open college website" in query:
            
            webbrowser.open("https://www.bitcollege.in")
            speak("Opening Bengal Institute of technology college website ")
            
        elif 'open offbeat' in query:
            webbrowser.open("https://tigtsd.offbeateducation.com/")
            speak("Opening Techno India groups offbeat student portal ")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google ")
            
        elif 'open makaut portal' in query:
            webbrowser.open("https://makaut1.ucanapply.com/smartexam/public")
            speak("Opening Makaut student portal")
            
        elif 'open makaut syllabus' in query:
            webbrowser.open("http://makautexam.net/aicte_details/Syllabus/BTECH.pdf")
            speak("Opening Makaut 1st Semester Syllabus")
            
        elif 'open calculator' in query:
            webbrowser.open("https://www.calculator.net") 
            speak("Opening Calculator ")
            
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")  
            speak("Opening whatsapp web")

        elif 'play music' in query:
            
            A =(random.randint(0,2))
            music_dir = "C:\\Users\\Siddhnat\\Desktop\\Chatbot"
            speak("Opening music")
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[A]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query: 
            codePath = "C:\\Users\\Siddhnat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
