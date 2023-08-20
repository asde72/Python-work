names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
try:
    index = int(input("Enter a list index between 0 and 9: "))
    name = names[index]
    print("The name at index", index, "is", name)
except IndexError as error_in_names:
    if index < 0:
        print("Index Invalid. Value too small. The first name is", names[0])
    else:
        print("Index Invalid. Value too large. The first name is", names[-1])