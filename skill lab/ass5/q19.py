password = input("Enter password: ")
mobile = input("Enter mobile number: ")

if not password.isalnum():
	print("Password should be alphanumeric only")
else:
	print("Password is alphanumeric")

if mobile.isdigit() and len(mobile) == 10:
	print("Mobile number is valid")
else:
	print("Invalid mobile number")
