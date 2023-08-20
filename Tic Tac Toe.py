myList =[   ['E','E','E'],
            ['E','E','E'],
            ['E','E','E']
        ]
i = 0
p = 0


myList[0][0] = input("Enter X or O")
myList[0][1] = input("Enter X or O")
myList[0][2] = input("Enter X or O")
myList[1][0] = input("Enter X or O")
myList[1][1] = input("Enter X or O")
myList[1][2] = input("Enter X or O")
myList[2][0] = input("Enter X or O")
myList[2][1] = input("Enter X or O")
print(myList)

if (myList[0] == ['X', 'X', 'X'] or myList[1] == ['X', 'X', 'X'] or myList[2] == ['X', 'X', 'X']):[2][2] = input("Enter X or O")

if (myList[0] == ['X', 'X', 'X'] or myList[1] == ['X', 'X', 'X'] or myList[2] == ['X', 'X', 'X']):
    print ("X IS GOOD IN HORIZONTAL")
elif (myList[0] == ['O', 'O', 'O'] or myList[1] == ['O', 'O', 'O'] or myList[2] == ['O', 'O', 'O']):
    print("O IS GOOD IN HORIZONTAL")
if (myList[0][0] == myList [1][0] == myList[2][0] == 'X') or (myList[0][1] == myList [1][1] == myList[2][1] == 'X') or (myList[0][2] == myList [1][2] == myList[2][2] == 'X'):
    print('X IS GOOD IN THE VERTICAL')
if (myList[0][0] == myList [1][0] == myList[2][0] == 'O') or (myList[0][1] == myList [1][1] == myList[2][1] == 'O') or (myList[0][2] == myList [1][2] == myList[2][2] == 'O'):
    print('O IS GOOD IN THE VERTICAL')    
if (myList[0][0] == myList[1][1] == myList[2][2] == 'X') or (myList[0][2] == myList[1][1] == myList[2][0] == 'X'):
    print('X IS GOOD IN THE DIAGONAL')
if (myList[0][0] == myList[1][1] == myList[2][2] == 'O') or (myList[0][2] == myList[1][1] == myList[2][0] == 'O'):
    print('O IS GOOD IN THE DIAGONAL')