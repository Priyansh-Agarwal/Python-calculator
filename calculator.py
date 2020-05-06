op = input("What operation do you want to perform?")
num1 = float(input("Enter your first number?"))
num2 = float(input("Enter your second number?"))

if op =="+":
    print(num1+num2)

elif op=="-":
    print(num1-num2)

elif op=="/":
    print(num1/num2)

elif op=="*":
    print(num1*num2)

else:
    print("Invalid Operation")