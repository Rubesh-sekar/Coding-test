# Simple Calculator
def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Error"

a=float(input("Enter value:"))
b=float(input("Enter value:"))
operation=input()

if operation=="add":
    result=add(a,b)
elif operation=="subtract":
    result=subtract(a,b)
elif operation=="multiply":
    result=multiply(a,b)
elif operation=="divide":
    result=divide(a,b)
else:
    result="Invalid operation"

print("Result:", result)
