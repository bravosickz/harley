from testerspeech import speak
from testerspeech import ear 
from testerspeech import preak 
from rem2 import rem 
from gewgle import gewgle 
from gewgle import yewt
from woofers import woofers
from testerspeech import glassear

def greet():
    import datetime
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

import time
greet()
time.sleep(2)

speakconst = 0
misc1 = 0

while misc1 < 1:
    import clearconsol
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
        

