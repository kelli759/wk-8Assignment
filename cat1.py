number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))

operation = input("Enter operation (+, -, *, /): ")

# Perform the chosen operation
if operation == "+":
    result = (number1 + number2)
    print(number1+number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
