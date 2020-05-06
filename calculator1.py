op = input("What operation do you want to perform?")
num1 = float(input("Enter your first number?"))
num2 = float(input("Enter your second number?"))

if op =="+":
    print("Addition of the two numbers is",num1+num2)

elif op=="-":
    print("Subtraction of the two numbers is",num1-num2)

elif op=="/":
    print("Division of the two numbers is",num1/num2)

elif op=="*":
    print("Multiplication of the two numbers is",num1*num2)

else:
    print("Invalid Operation")