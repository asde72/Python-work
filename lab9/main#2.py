# Prolog
# Author:  Jordan Gaffney
# Email:  jgaffney5@gsu.edu
# Section: 058
'''
Purpose:
        format the persons name as lastName, firstInitial.middleInitial.
Pre-conditions (input): 
        Enter firstName middleName lastName
Post-conditions (output): 
        Output the name formatted name.
'''
Name = input("Enter Full name (middle optional):").split()

first_initial = Name[0][0]
if len(Name) == 3:
  middle_initial = Name[1][0]
  last_name = Name[2]
  print(f"{last_name}, {first_initial}.{middle_initial}.")

else:
  print(f"{Name[1]}, {first_initial}.")
