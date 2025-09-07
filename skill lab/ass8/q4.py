file_path = input("Enter the file path: ")
search_word = input("Enter the word to search for: ")
line_numbers = []
with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        if search_word in line:
            line_numbers.append(i)

print("Line numbers where the word appears:", line_numbers)