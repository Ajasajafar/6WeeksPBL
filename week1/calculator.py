# python3 
# Simple calculator which uses the command line interface 
import math

# Defining the inputs
while True:
    print("Number 1")
    a = operand1 = input()
    print("Input Operator")
    operator = input()
    print("Number 2")
    b = operand1 = input()

# Making it work with the conditional statements 
    try:
        if operator == '/':
            print(f"{int(a) / int(b)}")
        elif operator == '+':
            print(f"{int(a) + int(b)}")
        elif operator == '-':
            print(f"{int(a) - int(b)}")
        elif operator == '*':
            print(f"{int(a) * int(b)}")
        elif operator == '**':
            print(f"{int(a) ** int(b)}")
        elif operator == "//":
            print(f"{int(a) // int(b)}")
        elif operator.lower() == 'sin':
            print(f"{int(a) * math.sin(math.radians(int(b)))}")
        elif operator.lower() == "cos":
            print(f"{int(a) * math.cos(math.radians(int(b)))}")
        elif operator.lower() == "tan":
            print(f"{int(a) * math.tan(math.radians(int(b)))}")
        elif operator.lower() == 'log':
            print(f"{int(a) * math.log(int(b))}")
        elif operator == '%':
            print(f"{(int(a) / 100) * int(b)}")
        else:
            print("Invalid Operator") 
    except ZeroDivisionError or ValueError:
        print("Undifined")