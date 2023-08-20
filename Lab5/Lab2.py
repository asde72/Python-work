# ''' Read in first equation, ax + by = c '''
# a = int1
# b = int2
# c = equals
# ''' Read in second equation, dx + ey = f '''
# d = equatex
# e = equatey
# f = equaltwo





int1 = int(input("X coeffcient?"))
int2 = int(input("Y coeffcient?"))
equals = int(input("What are they equal to?"))
equatex = int(input("Second X coeffcient?"))
equatey = int(input("Second Y coeffcient?"))
equaltwo = int(input("What are they equal to?"))
x = 1
y = 1
solution = False
for x in range(-10,10):
      for y in range(-10,10):
        if(int1 == int2 == equals == equatex == equatey == equaltwo):
            solution = False
            break
          
        if( (int1*x)  + (int2*y) == equals and (equatex*x) + (equatey*y) == equaltwo ):

            print("x = ",x)
            print("y = ",y)
            solution = True
if(solution == False):
        print ("The solution is false")
        
