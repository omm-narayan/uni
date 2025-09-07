num = int(input("Enter a number: "))
n = int(input("Enter the position 'n' from the right: "))

digit = (num // (10 ** (n - 1))) % 10

print(f"The digit at position {n} from the right is: {digit}")