file_path = input("./data/notes.txt")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    num_words = len(content.split())
    num_chars = len(content)
    num_lines = content.count('\n') + 1

print("Number of words:", num_words)
print("Number of characters:", num_chars)
print("Number of lines:", num_lines)