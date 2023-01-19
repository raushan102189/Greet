import time
from gender_checker import gender_checker
name = input('What is your name? ')

def greet(name ):
    gender = gender_checker(name)
    current_time = time.ctime()
    print(current_time)
    greetings = ['Good morning!', 'Good afternoon!', 'Good evening!']
    time.sleep(1)
    print('>>> 3 second left')
    time.sleep(1)
    print('>>> 2 second left')
    time.sleep(1)
    print('>>> 1 second left')
    if current_time < '12:00:00':
        if gender == "male":
            print(greetings[0], name, "sir")
        elif gender == "female":
            print(greetings[0], name, "mam")
    elif current_time > '12:00:00' and current_time < '18:00:00':
        if gender == "male":
            print(greetings[1], name, "sir")
        elif gender == "female":
            print(greetings[1], name, "mam")
    else:
        if gender == "male":
            print(greetings[2], name, "sir")
        elif gender == "female":
            print(greetings[2], name, "mam")
    

greet(name)