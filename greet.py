# greet me good morning wtih random message with input name
import time
name = input('What is your name? ')

def greet(name ):
    import random
    greetings = ['Good morning!', 'Good day!', 'Good afternoon!', 'Good evening!']
    time.sleep(1)
    print('>>> 3 second left')
    time.sleep(1)
    print('>>> 2 second left')
    time.sleep(2)
    print('>>> 1 second left')
    print(random.choice(greetings)+ ' ' + name +' sir')

greet(name)