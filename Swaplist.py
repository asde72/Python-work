def swap(list_to_swap):
    temp = list_to_swap[0]
    list_to_swap[0] = list_to_swap[-1]
    list_to_swap[-1] = temp
values_list = input("Your List:").split(";")
swap(values_list)
print(values_list)