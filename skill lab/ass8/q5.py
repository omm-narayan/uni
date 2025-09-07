numbers = [10, 20, 30, 40, 50]
file_path = "./data/numbers.txt"
with open(file_path, 'w', encoding='utf-8') as f:
    for number in numbers:
        f.write(f"{number}\n")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    print("Numbers read from file:", content.splitlines())