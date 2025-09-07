try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as ve:
    print(f"Error: {ve}")
else:
    print(f"Your age is {age}")