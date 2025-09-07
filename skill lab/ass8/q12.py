try:
    num = float(input("Enter a number: "))
    square = num ** 2
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"The square of {num} is {square}")