# Python calculator without interface

operator = input("Enter an operator(+, -, *, /): ")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Enter a valid operator")
    operator = input("Enter an operator(+, -, *, /)")
num1 = float(input("Enter the first number of the equation: "))
while isinstance(num1, float) == False:
    print("Enter a valid number!")
    num1 = float(input("Enter the first number of the equation: "))
num2 = float(input("Enter the second number of the equation: "))
while isinstance(num2, float) == False:
    print("Enter a valid number!")
    num2 = float(input("Enter the second number of the equation: "))
if operator == "+":
    print(f"The sum of {num1} and {num2} is {round(num1 + num2, 3)}")
if operator == "-":
    print(f"The subtraction of {num1} and {num2} is {round(num1 - num2, 3)}")
if operator == "*":
    print(f"The multiplication of {num1} and {num2} is {round(num1 * num2, 3)}")
if operator == "/":
    print(f"The division of {num1} and {num2} is {round(num1 / num2, 3)}")
