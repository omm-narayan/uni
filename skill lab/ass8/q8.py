import os
path = "./data/notes.txt"
with os.fdopen(os.open(path, os.O_RDONLY), "r", encoding="utf-8") as f:
    content = f.read()
    num_words = len(content.split())
print("Number of words in the file:", num_words)