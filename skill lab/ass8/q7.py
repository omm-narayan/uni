import os

search_word = input("Enter the word to search for: ")
line_numbers = []

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data", "multiple_note.txt")

if not os.path.exists(file_path):
    print("File not found:", file_path)
else:
    with os.fdopen(os.open(file_path, os.O_RDONLY), "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if search_word in line:
                line_numbers.append(i)

print("Line numbers where the word appears:", line_numbers)
