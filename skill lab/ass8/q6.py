import os 

path = "./data/multiple_note.txt"
with open(path, 'r', encoding='utf-8') as f:
    string = f.read()
    line_count = string.count('\n') + 1
    print("Number of lines in the file:", line_count)