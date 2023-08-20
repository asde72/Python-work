a = []
b = int(input("How many numbers are there"))
i = 0
for num in range(b):
    i = i + 1
    place_holder = int(input((f'Number {i}?')))
    a.append(place_holder)
lower = int(input("What is the lower bounds?"))
Upper = int(input("What is the upper bounds?"))

for num in a:
    if num > Upper:
        a.remove(num)
    elif num - lower < 0:
        a.remove(num)
print(*a,sep=',')