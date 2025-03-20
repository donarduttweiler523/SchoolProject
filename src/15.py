import random
import string

def get_random_string(length=10):
    """Returns a random string of length `length`."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
