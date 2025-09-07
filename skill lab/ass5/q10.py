s = input("Enter a string: ").strip()
s_clean = s.lower()
rev = s_clean[::-1]
if s_clean == rev:
	print("String is palindrome")
else:
	print("String is not palindrome")

print("Actual:", s)
print("Reversed:", rev)
