def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven ):
    gas_cost = (miles_driven/miles_per_gallon) * dollars_per_gallon
    return gas_cost 
MPG = float(input())
DPG = float(input())
print(f'{driving_cost( MPG ,DPG,10):.2f}')
print(f'{driving_cost( MPG ,DPG,50):.2f}')
print(f'{driving_cost( MPG ,DPG,400):.2f}')