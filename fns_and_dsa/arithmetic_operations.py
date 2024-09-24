def perform_operation(num1, num2, operation):
    # Perform addition
    if operation == 'add':
        return num1 + num2

    # Perform subtraction
    elif operation == 'subtract':
        return num1 - num2

    # Perform multiplication
    elif operation == 'multiply':
        return num1 * num2

    # Perform division with division by zero check
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    # Handle invalid operation input
    else:
        return "Error: Invalid operation"
    
    