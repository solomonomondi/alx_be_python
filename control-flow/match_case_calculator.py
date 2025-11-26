Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation: 
    case "+":
        result = Num1 + Num2
    case "-":
        result = Num1 - Num2
    case "*":
        result = Num1 * Num2
    case "/":
        if Num2 != 0:
            result = Num1 / Num2
        else:
            result = "Error: Division by zero is not allowed."

    case _:
        result = "Error: Invalid operation selected."
print("The result is:", result)