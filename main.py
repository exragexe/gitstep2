#dev
num1=int(input("Enter first number: "))
num2= int(input("Enter second number: "))
if num2 > num1:
    print(num2, num1)
elif num2 < num1:
    print(num1, num2)
elif num1 == num2:
    print(num1, num2)
else:
    print("Error")