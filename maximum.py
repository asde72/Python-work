def find_max(num_1 , num_2):
    max_val = 0.0
    if (num_1 > num_2):
        max_val = num_1
    else:
        max_val = num_2
    return max_val
max_sum = 0.0
num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())
max_sum = find_max(num_a, num_b) + find_max(num_y,num_z)
print('max sum is:', max_sum)