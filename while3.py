#Prints all letters eccept e and s
i = 0
a = 'geeksforgeeks'

while i < len(a):

    if a[i] == 'e' or a[i] =='s':
        i += 1
        continue

print('Current Letter :', a[1])
i += 1