def add_numbers(a, b):
    """
    Add two numbers and return their sum.
    
    Args:
        a (int): First number to be added.
        b (int): Second number to be added.
        
    Returns:
        int: The sum of a and b.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract two numbers and return their difference.
    
    Args:
        a (int): First number to be subtracted from.
        b (int): Second number to be subtracted.
        
    Returns:
        int: The difference of a and b.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiply two numbers and return their product.
    
    Args:
        a (int): First number to be multiplied.
        b (int): Second number to be multiplied.
        
    Returns:
        int: The product of a and b.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide two numbers and return their quotient.
    
    Args:
        a (int): First number to be divided by.
        b (int): Second number to be divided.
        
    Returns:
        int: The quotient of a and b.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def calculate_square_root(num):
    """
    Calculate the square root of a given number using the math module.
    
    Args:
        num (int): The number to find the square root of.
        
    Returns:
        float: The square root of num.
    """
    import math
    return math.sqrt(num)

def main():
    # Example usage
    print("Addition:", add_numbers(3, 5))
    print("Subtraction:", subtract_numbers(10, 4))
    print("Multiplication:", multiply_numbers(2, 7))
    print("Division:", divide_numbers(8, 2))
    try:
        print("Square root of", num, "is", calculate_square_root(num))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
