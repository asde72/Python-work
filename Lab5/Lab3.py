list = []
adjust_list = []
list_length = int(input(("How many values are there")))
Value_Cap = list_length
Loop_Repeat = 0
Value_Number = 1
while Value_Cap > Loop_Repeat :
    print("Value",Value_Number,"?")
    list.append(float(input()))
    # print(list)
    Value_Number += 1
    Loop_Repeat += 1
# print(max(list))
#This gets list and divides it by the max value
for x in list:
    adjust_list.append(x/max(list))
rounded_list = [round(item,2) for item in adjust_list]
print(*rounded_list, sep= "\n") 
