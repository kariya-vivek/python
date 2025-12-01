def is_opposite(num1, num2):
    return num1 == -num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if is_opposite(num1, num2):
    print(f"{num2} is the opposite of {num1}")
else:
    print(f"{num2} is not the opposite of {num1}")
