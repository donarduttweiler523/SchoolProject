def get_random_integer(n):
    import random
    return random.randint(1, n)

def get_random_string(length):
    import string
    letters = string.ascii_lowercase + string.digits
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result
