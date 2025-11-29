def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform - 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
        float or str: Result of the operation, or error message for division by zero
    """
    operation = operation.strip().lower()
    
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            else:
                return num1 / num2
        case _:
            return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."