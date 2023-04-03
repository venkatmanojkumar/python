def argument(message, default = '-'):
    line = default * len(message)
    print(line)
    print(message)
    print(line)

argument("message")

#default arguments

import time

def current_time(time = time.ctime()):
    print(time)

current_time()

# mutable default value 

def add_spam(menu=[]):
    menu.append("spam")
    print(menu)

add_spam()

# immutable default value 

def immutable(menu = None):
    if menu is None:
        menu = []
        menu.append('spam')
        print(menu)

immutable()