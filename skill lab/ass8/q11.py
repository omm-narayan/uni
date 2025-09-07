try:
    num = float(input("Enter numerator: "))
    denom = float(input("Enter denominator: "))
    result = num / denom
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Result: {result}")