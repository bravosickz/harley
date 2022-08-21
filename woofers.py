from testerspeech import preak
from testerspeech import ear
from testerspeech import speak

def woofers():
    import pywhatkit 
    preak("Song?") 
    comm = ear()
    msg = "Sure, playing " + comm 
    preak(msg)
    pywhatkit.playonyt(comm)
