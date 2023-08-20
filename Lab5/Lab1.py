from ast import increment_lineno
number_1 = int(input("What is the first number?"))
number_2 = int(input("What is the second number?"))
increment = number_1

if number_1 < number_2:
    print(increment)
    while increment <= number_2:
        if increment + 5 < number_2:
            increment += 5
            print(increment)
        else:

            print(number_2)
            break
else:
    print("Second integer cant be less or equal to than the first one")