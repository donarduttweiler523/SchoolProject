def multiply_numbers(a: float, b: float) -> float:
    result = a * b
    return result

def main():
    user_input1 = float(input("Enter the first number: "))
    user_input2 = float(input("Enter the second number: "))
    
    result = multiply_numbers(user_input1, user_input2)
    print(f"The product of {user_input1} and {user_input2} is: {result}")

if __name__ == "__main__":
    main()
