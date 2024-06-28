def calculator():

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    

    print("Select an operation:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")
    
    operation = input("Enter the number corresponding to the operation: ")
    

    if operation == '1' or operation == '+':
        result = num1 + num2
        op_symbol = '+'
    elif operation == '2' or operation == '-':
        result = num1 - num2
        op_symbol = '-'
    elif operation == '3' or operation == '*':
        result = num1 * num2
        op_symbol = '*'
    elif operation == '4' or operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op_symbol = '/'
    else:
        print("Invalid operation choice. Please select 1, 2, 3, or 4.")
        return
    

    print(f"The result of {num1} {op_symbol} {num2} is: {result}")

# Run the calculator
calculator()
