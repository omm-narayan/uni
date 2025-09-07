print("calculating (a-b)/(c-d)")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if c-d == 0:
    print("Error: division by zero")
else:
    X = (a-b)/(c-d)
    print(f"Result: {X}")
