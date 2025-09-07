import os
path = "./data/notes.txt"
try:
    with os.fdopen(os.open(path, os.O_RDONLY), "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("File operation complete")
