import os
path = "./data/user_input.txt"
try:
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT), "w", encoding="utf-8") as f:
        user_input = input("Enter some text: ")
        f.write(user_input + "\n")
except OSError as e:
    print(f"Error: Could not open or write to the file. {e}")
else:
    print("Input written to file successfully.")