import calculator

num1 = int(input("Write a number: "))
num2 = int(input("Write another number: "))
operation = input("What operation would you like to perform on the numbers?: ")
if operation == "+" or "add":
    print("The answer is " + nr1)
elif operation =="-" or "subtract":
    print("The answer is " + nr2)
elif operation == "*" or "multiply":
    print("The answer is " + nr3)
elif operation == "//" or "divide":
    if num1 or num2 == 0:
        raise ZeroDivisionError
    print("The answer is " + nr4)
