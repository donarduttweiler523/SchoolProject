def add(x, y):
    """Add two numbers x and y"""
    result = x + y
    return result

def subtract(x, y):
    """Subtract two numbers x and y"""
    result = x - y
    return result

def multiply(x, y):
    """Multiply two numbers x and y"""
    result = x * y
    return result

def divide(x, y):
    """Divide two numbers x and y"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        result = x / y
        return result

print(add(5, 3))       # Output: 8
print(subtract(10, 4))  # Output: 6
print(multiply(7, 2))   # Output: 14
print(divide(9, 0))     # Output: Error: Cannot divide by zero
