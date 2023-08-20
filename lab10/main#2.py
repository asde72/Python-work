import math
# Use mod or something to detect middle number range of list mod 2 should give middle number
def calculator(length):
    Odd_middle = (math.floor(length/2))
    return Odd_middle
a = []

i = 0
b = int(input("How many numbers are there"))
while b > 9:
    print("""Too many inputs
    Try again!""")
    b = int(input("How many numbers are there"))
2
for num in range(b):
    i = i + 1
    place_holder = int(input((f'Number {i}?')))
    a.append(place_holder)

print(f"Middle item: {a[calculator(b)]}")