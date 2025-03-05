import random
def get_random_code(length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(length):
        code += alphabet[random.randint(0, len(alphabet) - 1)]
    return code