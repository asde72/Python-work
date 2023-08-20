def feet_to_steps(feet):
    steps = feet/2.5
    return int(steps)
def main():
    feet_input = float(input("How many feet have you walked?"))   
    
    print(f"You've walked aproximately: {feet_to_steps(feet_input)} steps")

main()