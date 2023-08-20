# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5
# Section: 058
'''
  Purpose:
    Adjust the list_of_values by dividing all list_of_values by the largest value. 
  Pre-conditions (input): 
    Enter an integer indicating the number of floating-point list_of_values that follow. Enter the floating-points.
  Post-conditions (output): 
    Adjusted list_of_values with two digits after the decimal point.
'''
# Design and implementation

def main():

    int_input = int(input("Enter the amount of floating-point values: "))

    #Input the floating-point values
    list_of_values = [ ]
    for j in range(int_input):
        value = float(input("What is the value?: "))
        list_of_values.append(value)

    max_values = max(list_of_values)

    #Adjust list_of_values by by dividing all values by the largest value.
    for value in list_of_values:
        new_value_list = value / max_values
        print(f"{new_value_list:.2f}")

main()
# end of program file
