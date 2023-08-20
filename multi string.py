#Python3 code to demonstrate woking of
# move word to rear end
#using replace() + "+" operator

#initializing string
test_str = 'Python is the brest for geeks'

#printing the original string
print("The original string is : " + str(test_str))

#initializing substring
sub_str = 'best'

#move word to rear end
#using replace() + "+" operator

res = test_str.replace(sub_str,"") + str(sub_str)

#printing final result
print('The string after word removal : ' + str(res))
