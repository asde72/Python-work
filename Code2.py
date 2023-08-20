def multiplyList(myList): #new function named multiply_List
    result = 1#sets result variable equal to 1
    for x in myList: #Loops for every vlaue in the List
        result = result * x #multiply result by increasing.
    return result
list1 = [1, 2, 3] #defines list 1
list2 = [3, 2, 4] #defines list 2
print(multiplyList(list1)) #prints multiplied list 1
print(multiplyList(list2)) #prints multiplied list 2
