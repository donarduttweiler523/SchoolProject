def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

school_project_data = [12.5, 23.7, 45.6, 67.8, 89.1]
average_score = calculate_average(school_project_data)
print("The average score is:", average_score)
