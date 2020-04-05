'''
num1 =  input("Enter a number: ")
num2 =  input("Enter a 2nd number: ")
result = float(num1) + float(num2)
print(result)
'''

#advance calculator
num1 = float(input("Enter first number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op =="*":
    print(num1 * num2)
else:
    print("Invalid operator")
