import datetime
from rem2 import rem

'''
Reminder list
------------------
Inputs: Hour, Minutes (in 24-hour format)
Outputs: Notification pop-up at time input
Modules: rem2 & reminder
Image: (in folder) uses relative path, so device independent
'''

#time parameteres
remhr = int(input("Enter hour: "))
remmin = int(input("Enter minutes: "))

#User comment
tx = input("Enter your reminder here: ")

#Setting the reminder
print("Confirm [Y/N]")
key = input()
if key == "Y":
    print("Your reminder has been successfully set")

    gate = 0
    while gate < 1:
        if remhr == datetime.datetime.now().hour:
            if remmin == datetime.datetime.now().minute:
                rem(tx)
                gate += 1
