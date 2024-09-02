def calculator():
    print("Welcome to the Simple Calculator!")

    # Prompt user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Display operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt user to choose an operation
    operation = input("Enter the operation number you want to perform (1/2/3/4): ")

    #  calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")

    elif operation == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")

    elif operation == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")

    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")

    else:
        print("Invalid operation choice! Please select a number between 1 and 4.")

# Run the calculator
calculator()
