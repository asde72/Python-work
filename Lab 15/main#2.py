from itertools import permutations
def print_all_permutations(permList, nameList):
# TODO: Implement method to create and output all permutations of the list of names.
    keymaker = len(nameList)
    Key_List = []
    for x in range(keymaker):
        Key_List.append(x+1)
    combination_Dictionary = dict(zip(nameList,Key_List))
    permList = permutations(combination_Dictionary.keys())
    for i in list(permList):
        print(i)    
if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)