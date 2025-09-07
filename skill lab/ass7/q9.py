def to_uppercase(word):
    return word.upper()

words = ["hello", "world", "python"]
uppercase_words = list(map(to_uppercase, words))
print(uppercase_words)
