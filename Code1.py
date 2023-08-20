def multiplyList(myList) : #new function named multiply_List
    result = 1 #sets result variable equal to 1
    for i in range(0,len(myList)): #repeats loop depending on lengrh of list.
        result = result * myList[i] #multiplies the list by an increasing value  
    return result
list1 = [1, 2, 3] #defines list 1
list2 = [3, 2, 4] #defnines list 2
print(multiplyList(list1)) #prints list 2 that has been multiplied by the multify function  
print(multiplyList(list2)) #prints list 1 that has been multiplied by the multify    function  
