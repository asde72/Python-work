name = 'Wayne Rooney'
goals = 36

#Use default empty space fill character
print(f'{name:<16}{goals:>6}')
# User '0' as a fill character for score
print(f'{name:<16}{goals:0>6}')
#Use '_' as fill character for name
print(f'{name:_<16}{goals:0>6}')
