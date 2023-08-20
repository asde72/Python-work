import math

def max_magnitude(user_val1, user_val2 , user_val3):
    max = 0
    user_val1 = float(input())
    user_val2 = float(input())
    user_val3 = float(input())
   
   
    if math.fabs(user_val1) < math.fabs(user_val2) and math.fabs(user_val3) < math.fabs(user_val2):
        max = user_val2
    elif math.fabs(user_val2) < math.fabs(user_val3) and math.fabs(user_val1) < math.fabs(user_val3) :
        max = user_val3
    elif math.fabs(user_val2) < math.fabs(user_val1) and math.fabs(user_val3) < math.fabs(user_val1) :
        max = user_val1
    return(max)

print(max_magnitude(user_val1 = 0, user_val2 = 0, user_val3 = 0))
