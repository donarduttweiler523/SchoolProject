def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    # Example usage
    student_scores = [85, 90, 76, 92, 88]
    print(calculate_average(student_scores))
except ValueError as e:
    print(e)

# Uncomment the following line to test the function with an empty list of scores
