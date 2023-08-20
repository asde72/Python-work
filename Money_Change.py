# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5@gsu.edu
# Section: 0580
'''
  Purpose: 
      converting changes to dollars.
  Pre-conditions (input): 
      number of changes
  Post-conditions (output): 
      converted changes (quarters, dimes, nickels, and pennies) to dollars
      
'''


def main():
# Design and implementation


#  1.  Output a message to identify the program, and a blank line
    print("Conversion of changes to dollars")
    print()


#  2.  Input changes from user (quarters, dimes, nickels and pennies)
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))




#  3.  Calculate the dollars amounts.
    dollars = (quarters*25 + dimes*10 + nickels*5 + pennies) / 100.0
    


#  4. Output resulting changes converted to dollars. 
    print()
    print(f'{quarters} quarters,{dimes} dimes,{nickels} nickels,{pennies} pennies ' "are equal to {:.2f} dollars".format(dollars))


main()
# end of program file
# Indent error on line 26
# The program cant run because three variables on lines 30 and 36 are not defined
#  name "dimes" , "nickles" , "pennies" is not defined
# create variables dimes nickles and pennies and set the equal to a given input 
