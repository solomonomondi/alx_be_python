# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'multiply':
        return num1 * num2
    if operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."