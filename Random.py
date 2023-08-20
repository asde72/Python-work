# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    random.seed(900)
    rand_num = random.randint(1, 100)

    # TODO: Read numbers and compare to random number
    if num < rand_num:
        print(f"{num} is too low. Random number was {rand_num}.")
    elif num > rand_num:
        print(f"{num} is too high. Random number was {rand_num}.")
    else:
        print(f"{num} is correct.")

if __name__ == "__main__":
    random.seed(900)
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)



