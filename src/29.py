def add_numbers(x, y):
    return x + y

def subtract(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result
