# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5@gsu.edu
# Section: 058
'''
  Purpose:
    Phone number breakdown


  Pre-conditions (input): 
       (Enter the 10-digit phone number)
  Post-conditions (output): 
      Breakdown of phone number (area code, prefix, line number)
      
'''


def main():
# Design and implementation


#  1.  Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, line number")
    print()


#  2.  Input the 10-digit phone number
    Phone_number = int(input ())




#  3.  Breakdown the phone number
    phone_str = str(Phone_number) 
    area_code = phone_str[0:3]
    prefix = phone_str[3:6]
    line_number = phone_str[6:10]

#  4. Output breakdown to area code, prefix, line number
   # print()
    print  (f'({area_code})-{prefix}-{line_number}')
    print (f'Phone number is converted to area code ={area_code} , prefix ={prefix} , line number ={line_number}')
main()
# end of program file 
# 39 remove apostrophies and add them around %s invalid character '‘' (U+2018)
# line 28 incorrect indents IndentationError: unexpected indent fix indent
# line 39 missing parenthesies
# line 39 define variables area_code , prefix ,line_number 
