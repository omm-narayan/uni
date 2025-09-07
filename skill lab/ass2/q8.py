print("calculating x1 and x2 for ax1 + bx2 = m & cx1 + dx2 = n :")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
m = int(input("Enter m: "))
n = int(input("Enter n: "))

if (a * b - c * d == 0):
    print("No solution")
else:
    x1 = (m * d - n * b) / (a * d - b * c)
    x2 = (n * a - m * c) / (a * d - b * c)
    print(f"x1 = {x1}, x2 = {x2}")
