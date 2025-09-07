n = int(input("Enter the number of Fibonacci terms to print: "))
a, b = 0, 1

print(f"\nFirst {n} Fibonacci numbers:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

    