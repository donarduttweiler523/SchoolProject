import random

def get_random_number(low: int, high: int) -> int:
    """Returns a random integer between low and high, inclusive."""
    return random.randint(low, high)