import random
def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    total = how_many
    max = max_num   
    randList = [random.sample(range(0,max), total)]
    print(f'{randList}, retries={retries}')

if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())
    retries = 1
    random.seed(seed)
    unique_random_ints(how_many,max_num)
