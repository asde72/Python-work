def get_numbers(number1,loop_length):
    for x in range(loop_length):
        number1.append(int(input("What number")))
    return number1
v = int(input("How many numbers are there?"))
calzone = []
new_list = []   
new_list = get_numbers(calzone,v)
print(new_list)
z = max(new_list)
c = float((sum(new_list)/len(new_list)))
print(z)
print(round(c))