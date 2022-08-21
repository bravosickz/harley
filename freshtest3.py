import time
from numba import jit 
star = time.time()
import pyttsx3
import speech_recognition as sr
import datetime
from playsound import playsound
import time 
from plyer import notification
@jit(nopython=True)
def main():
    star = time.time()
    engine = pyttsx3.init('sapi5') #microsoft api sapi5
    voices = engine.getProperty('voices')
    print(voices[1].id) 
    engine.setProperty('voice', voices[1].id) #zira voice
    def clearconsol():
        import subprocess
        import os
        import sys
        import time
        time.sleep(2)
        os.system("cls") #clear the console
        print("*****************************")

    def rem(word):
        import time
        from plyer import notification

        notification.notify(
            title = "Harley DA",
            message = word,
            app_icon = "coffee-2-128.ico",
            timeout = 30
)
    

    def speak(audio):
        engine = pyttsx3.init('sapi5') #microsoft api sapi5
        voices = engine.getProperty('voices')
        print(voices[1].id) 
        engine.setProperty('voice', voices[1].id) #zira voice
        engine.say(audio)
        engine.runAndWait()
    
    def preak(s):
        rem(s)
        speak(s)
        print(s)
    
    def ear():
        k = 0
        while k < 1:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1 #duration for how long it records
                audio = r.listen(source) #listen
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in') #translate stt
                print(query) #result
                return query
                break
            except Exception as e:
                continue
    def glassear(): #ear() but without print functions, good for bg listening
        k = 0
        while k < 1:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1 #duration for how long it records
                audio = r.listen(source) #listen
            try:
                query = r.recognize_google(audio, language='en-in') #translate stt
                return query
                break
            except Exception as e:
                continue

    
    def woofers():
        import pywhatkit 
        preak("Song?") 
        comm = ear()
        msg = "Sure, playing " + comm 
        preak(msg)
        pywhatkit.playonyt(comm)
    def greet():
        n = datetime.datetime.now()
        strmsg = "it is " + n.strftime("%Y-%m-%d %H:%M")
        if n.hour in range(4,12):
            preak("Good morning!")
            rem(strmsg)
        #now.strftime("%Y-%m-%d %H:%M:%S"))
        elif n.minute in range(12,5):
            preak("Good afteroon!")
            preak(strmsg)
        else:
            preak("Good evening")
            preak(strmsg)
    def gewgle():
        preak("what do you want to google?")
        y = str(ear())
        import webbrowser as w
        msg = "searching for "+ y
        preak(msg)
        googlink = "https://www.google.com/search?q=" + y.lower()
        w.open_new_tab(googlink)
        clearconsol()
    def yewt():
        preak("What do you want to watch?")
        y = str(ear())
        import webbrowser as w
        msg = "searching for "+ y
        preak(msg)
        yewlink = "https://www.youtube.com/results?search_query=" + y.lower()
        w.open_new_tab(yewlink)
        clearconsol()


#main
main()
greet()

end = time.time()
print(end-star)

'''
speakconst = 0
misc1 = 0
while misc1 < 1:
    clearconsol()
    speakgate = glassear() #listens in the background
    if 'harley' in speakgate.lower(): #if speech contains harley
        while speakconst < 1: 
            preak("speak now please...")
            print("Listening...")
            x = ear()
            if "google" in x.lower():
                gewgle()
            elif "alarm" in x.lower(): 
                import alarmClock
            elif "youtube" in x.lower():
                yewt()
            elif "play" in x.lower():
                woofers()
            elif "thank" in x.lower():
                preak("Glad to be of help")
                break #break 1st while loop
        
         #clear the console
        continue #back to line 32
    else:
        continue
'''


