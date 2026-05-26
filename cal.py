num1 = float(input("первое число:"))
operation = input("операция +, -, *, /,:")
num2 = float(input("второе число : "))

if operation == "+":
    print(num1+num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

else:
    print("неизвестная операция")
