import random

# Constants Variables
low_limit = 1
high_limit = 20
max_attempts = 4


def randomizer(lower_limit, upper_limit) :
    return random.randint(lower_limit, upper_limit)
