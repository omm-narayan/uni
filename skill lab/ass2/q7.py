c = int(input("Enter cost price: "))
d = int(input("Enter selling price: "))

if d < c:
    print("Loss")
elif d == c:
    print("No profit, no loss")
else:
    print("Profit")
