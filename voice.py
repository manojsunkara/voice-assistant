import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
                
            
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        talk('cuttent time is ' + time)

    elif 'search' in command:
        person = command.replace('wilipedia', '')
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('am good,how about you')
    elif 'are you single' in command:
        talk('am a virtual assistant')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
        
                


run_jarvis()
