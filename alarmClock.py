import datetime 
from testerspeech import preak
from testerspeech import ear
from testerspeech import speak
import time
def nexrem(big,small):
    from winotify import Notification, audio
    ping = Notification(app_id="Harley: personal assistant",
                        title=big,
                        msg=small,
                        duration="long")

    ping.set_audio(audio.LoopingAlarm6,loop=False)
    ping.add_actions(label="Dismiss")
    ping.show()
#user inputs
def alarm():
    preak("Please set your alarm time: ")
    alarmHour = int(input("Hours: "))
    alarmMinute = int(input("Minutes: "))
    preak("time format?")
    AmPm = input("am/pm : ")

    #12 hour format
    if AmPm == "pm":
        alarmHour += 12
    #confirmation message
    msg = "Alarm set for "+ str(alarmHour) + ":" + str(alarmMinute)
    preak(msg)

    #setting the alarm
    while True:
        if alarmHour == datetime.datetime.now().hour:
            if alarmMinute == datetime.datetime.now().minute:
                nexrem("Alarm","Your Alarm's ringing!")
                break


