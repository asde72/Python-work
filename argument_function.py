def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    # storing function as a variable
    greeting = func(""" Hi I am created by a function
                        passeed as an argument""")
    print (greeting)

greet(shout)
greet(whisper)