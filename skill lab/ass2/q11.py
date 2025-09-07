a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choice = input("Enter choice (+, -, *, /): ")

if choice == '+':
    print(a + b)
elif choice == '-':
    print(a - b)
elif choice == '*':
    print(a * b)
elif choice == '/':
    print(a / b)
else:
    print("Invalid choice")
