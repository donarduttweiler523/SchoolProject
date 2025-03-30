def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return average

school_project_scores = [95, 82, 76, 91, 89]
average_score = calculate_average(school_project_scores)
print("The average score of the school project is:", average_score)
