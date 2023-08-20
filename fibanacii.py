def fibonacci(n):
    # Increment and Starting Value 
    First = 0
    Second = 1

    #Check if input is lower than 0
    if n < 0:
        return -1
    #Check if input is 0 (sequence would stay 0)
    elif n == 0:
        return Second
    #Otherwise Calculates The Sequence number by adding each value by the previous amount n amount of times
    else: 
        for i in range(1, n):
            Sequencer = First + Second
            First = Second
            Second = Sequencer
    #Defines the final output        
        Final = Second
        return Final
#Takes input from user
input = int((input("What sequence are you looking for?")))
#Calls function parameter based on input
new_value = fibonacci(input)

#Prints what the sequence number is.
print(f'fibonacci({input}) is {new_value} ')