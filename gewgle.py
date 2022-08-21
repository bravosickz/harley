from testerspeech import ear
from testerspeech import speak
from testerspeech import preak

def gewgle():
    preak("what do you want to google?")
    y = str(ear())
    import webbrowser as w
    msg = "searching for "+ y
    preak(msg)
    googlink = "https://www.google.com/search?q=" + y.lower()
    w.open_new_tab(googlink)
    import clearconsol

def yewt():
    preak("What do you want to watch?")
    y = str(ear())
    import webbrowser as w
    msg = "searching for "+ y
    preak(msg)
    yewlink = "https://www.youtube.com/results?search_query=" + y.lower()
    w.open_new_tab(yewlink)
    import clearconsol
    

