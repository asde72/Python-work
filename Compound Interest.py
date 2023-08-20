
# Prolog
# Author: Jordan Gaffney
# Email: jgaffney5@gsu.edu
# Section: 22587
import math
#  main function
def main():
    # Display introductory message
    P = float(input(" What is the principal amount? ($) 2500.00)"))
    Rate = float(input( "What is the annual interest rate? (%) 6.0"))
    Interest_Rate = Rate / 100
    Compound = float(input("What is the number of times per year is the interest applied?"))
    years = float(input("What is the number of years interest applied? 2"))
    I = (P * math.pow(1+ (Interest_Rate/Compound),(Compound*years)) )
    print(f"""The total amount accrued, principal plus interest, 
    with compound interest on a principal ${P} at a rate of {Rate}% per year compounded {Compound} times per year over
    {years} years is ${I:.2f}""")

main()