def add_numbers(x, y):
    """
    Adds two numbers x and y.
    
    Parameters:
    x (int): The first number to be added.
    y (int): The second number to be added.
    
    Returns:
    int: The sum of x and y.
    """
    return x + y

def print_numbers(numbers):
    """
    Prints the numbers in a given list.
    
    Parameters:
    numbers (list of int): A list of integers.
    """
    for num in numbers:
        print(num)

# Example usage
if __name__ == "__main__":
    # Add two numbers
    sum = add_numbers(5, 3)
    print(f"The sum is: {sum}")
    
    # Print a list of numbers
    numbers = [10, 20, 30]
    print_numbers(numbers)
