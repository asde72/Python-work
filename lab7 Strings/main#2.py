# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5
# Section: 058
'''
  Purpose:
     Write a program that takes a simple password and makes it stronger by replacing characters using
        the key below, and by appending "!" to the end of the input string
  Pre-conditions (input): 
       Enter a password.
  Post-conditions (output): 
      Replace characters and add "!" to the end of the input string.
'''
def main():
    #input
    password = input("Enter your password: ")
    stronger_passcode = []
    shifter = 0
    #replace characters with 1 @ M 8 $ 
    while shifter < len(password):
        if password[shifter] == 'i':
            stronger_passcode.append('1')
        elif password[shifter] == 'a':
            stronger_passcode.append('@')
        elif password[shifter] == 'm':
            stronger_passcode.append('M')
        elif password[shifter] == 'B':
            stronger_passcode.append('8')
        elif password[shifter] == 's':
            stronger_passcode.append('$')
        else:
            stronger_passcode.append(password[shifter])
        shifter += 1

    stronger_passcode.append('!')
    #convert the list into a string
    str_passcode= ""
    for shifter in stronger_passcode:
        str_passcode+=shifter

    # print password with converted list string
    print(f'Adjusted password is: {str_passcode}')



main()
