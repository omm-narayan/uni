string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

result = ''.join([c for c in (string1 + string2) if c.isupper() and c.isalpha()])

print("Actual string1:", string1)
print("Actual string2:", string2)
print("Resultant uppercase concatenation:", result)
