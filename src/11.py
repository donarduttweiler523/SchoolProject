import random

def get_random_string(length):
    # Use the choice method to generate a string of letters and numbers
    letters_and_numbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(letters_and_numbers) for _ in range(length))

def get_random_string_with_special_characters(length):
    # Use the choice method to generate a string of letters, numbers, and special characters
    letters_and_numbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    special_characters = '!@#$%^&*()-=_+'
    return ''.join(random.choice(letters_and_numbers + special_characters) for _ in range(length))

def get_random_email(domain):
    # Use the choice method to generate a string of letters and numbers, with a random length between 6 and 12
    email = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(random.randint(6, 12)))
    # Add the domain to the end of the email
    return f"{email}@{domain}"

def get_random_password(length):
    # Use the choice method to generate a string of letters and numbers, with a random length between 8 and 16
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(random.randint(8, 16)))
    # Add a special character to the end of the password
    return f"{password}{random.choice('!@#$%^&*()-=_+')}"