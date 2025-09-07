email = input("Enter email address: ")
if '@' in email:
	print("Index of @:", email.index('@'))
else:
	print("Invalid email")
