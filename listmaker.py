remgate = 1

while remgate > 0:
    fname = 'list'+ str(remgate) #list1, list2, list3...
    fobj = open(fname,'a+')
    fgate = 1
    while fgate > 0:
        reminder = input()
        fobj.writelines(reminder)
        conf = input("close list (y/n)?")
        if conf.lower() == 'y':
            break
        else:
            continue
    confPR = input('''
    1. close reminders
    2. fresh list
    3. access an old list
    ''')

    if confPR.lower() == 1:
        break 
    elif confPR.lower() == 2:
        print("switching to a fresh list")
        continue 
    elif confPR.lower() == 3:
        oldgate = 1
        while oldgate > 0:
            try:
                oldname = input("Enter name of old list: ")
                break
            except:
                print("sorry, couldn't find your list, try again!")
                continue
        oldext = oldname + '.txt'

        oldgate2 = 1
        while oldgate2 > 0:
            confPRXV = input('''
            1. read file
            2. add reminders
            3. close ''')
            if confPRXV == 1:
                fold = open(oldext,'r')
                fold.read()
                continue
            elif confPRXV == 2:
                fold = open(oldext,'a+')
                fgate2 = 1
                while fgate2 > 0:
                    reminder2 = input()
                    fold.writelines(reminder)
                    conf = input("close list (y/n)?")
                    if conf.lower() == 'y':
                        break
                    else:
                        continue
                continue
            elif confPRXV == 3:
                print("closing...")
                break
        break
        


