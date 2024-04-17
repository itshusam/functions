def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y
    
num1 = float(input("Enter the first number!"))
num2 = float(input("Enter the second number!"))
operation = input("choose! (+ for addition, - for subtraction, * for multiplication, / for division)")

if operation == '+':
    result = addition(num1, num2)
elif operation == '-':
    result = subtraction(num1, num2)
elif operation == '*':
    result = multiplication(num1, num2)
elif operation == '/':
    result = division(num1, num2)
print (result)