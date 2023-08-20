# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5
# Section: 058
'''
  Purpose:
    Write a program that takes in a line of text as input, and outputs that line of
    text in reverse.
  Pre-conditions (input): 
       Enter a line of text (ending when the user enters "Done", "done", or "d" for the line of text.)
  Post-conditions (output): 
      print the line of text in reverse.
'''
def main():
# Design and implementation
  while True:
        #input
      string_text = input("Enter a line of text: ")
      #check for end
      if string_text in ["d", "D","done","Done"]:
          print("COMPLETE")
          break
      else:
            print(string_text[::-1])

main()
# end of program file