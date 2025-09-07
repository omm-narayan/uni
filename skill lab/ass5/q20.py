pwd = input("Enter password to check strength: ")

has_lower = any(c.islower() for c in pwd)
has_upper = any(c.isupper() for c in pwd)
has_digit = any(c.isdigit() for c in pwd)

if has_lower and has_upper and has_digit:
	print("Strong password")
else:
	print("Weak password")
