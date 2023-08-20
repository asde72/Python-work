w# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5@gsu.edu
# Section: 058
'''
Purpose:
       Swap the first value with the second value, and the third value with the fourth value. 
Pre-conditions (input): 
        Enter four integers as parameters
Post-conditions (output): 
        Output the the swapped values.
'''
def swap_values(user_val1, user_val2, user_val3, user_val4):
    placeholder1 = user_val1
    placeholder2 = user_val3
    user_val1 = user_val2
    user_val3 = user_val4
    user_val2 = placeholder1
    user_val4 = placeholder2
    
    return user_val1, user_val2, user_val3, user_val4

def main():
    user_val1= int(input(" First value?"))
    user_val2 = int(input(" Second value?"))
    user_val3 = int(input(" Third value?"))
    user_val4 = int(input(" Fourth value?"))

    swapped_function = swap_values(user_val1, user_val2, user_val3, user_val4)

    print(f"{swapped_function[0]}, {swapped_function[1]}, {swapped_function[2]}, {swapped_function[3]}")
main()
