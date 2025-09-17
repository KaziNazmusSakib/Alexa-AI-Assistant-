import speech_recognition as sr 
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listner = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replacce('alexa' , '')
 
    except:
        pass
    return command    

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)  
    
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    
    elif 'sleep' in command:
        talk('Sorry if you ask me again, I will  cook your brain, So dont disturb me.')   
    else:
        talk('I did not get it but I am going to search it for you.')
        pywhatkit.search(command)       

while True:
    run_alexa()