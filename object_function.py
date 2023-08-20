#python program to illustrate functions can be used as objects

def shout(text):
        return text.upper()
print(shout('Hello'))
yell = shout
print(yell('Hello'))