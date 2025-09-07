num = int(input("Enter a number: "))
if num >= 0:
    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num:
        print(f"{num} is a perfect square.")
    else:
        print(f"{num} is not a perfect square.")
else:
    print("Negative numbers cannot be perfect squares.")