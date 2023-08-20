#break the loop as soon as it sees'e'
# or s
i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[1] == 'e' or a[1] =='s':
        i += 1
        break
    print('Current Letter :', a[1])
    i += 1