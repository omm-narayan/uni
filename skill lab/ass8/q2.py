path = "./data/multiple_note.txt"
with open(path, 'r', encoding='utf-8') as f:
	string = f.read()

new_str = string.splitlines()
print(new_str)