#Input numbers and operations
number1 = 5
number2 = 10
operation = ('*')

# Mathematical operations
if operation == '+':
    addition= number1 + number2
    print(f"{number1} + {number2} = {addition}")
    
elif operation == '-':
    subtraction = number1 - number2
    print(f"{number1} - {number2} = {subtraction}")
    
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
    
elif operation == '/':
    if number2 != 0:
        division: float = number1 / number2
        print(f"{number1} / {number2} = {division}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +,-,*, or /.")