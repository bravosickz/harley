import datetime 
from playsound import playsound
from rem2 import rem
from testerspeech import preak 
#user inputs
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
            rem("Your Alarm's ringing!")
            playsound("Seirei.mp3")
