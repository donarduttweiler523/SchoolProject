import random

def random_code():
    num = random.randint(0, 10)
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
