# Python program to demonstate
# while-else loop
i = 0
while i < 4:
    i += 1
    print()
else: #executed because no break in for
    print("No break\n")

i = 0
while i < 4:
    i+= 1
    print(i)
    break
else: #Not executed as there is a break
    print("No break")
