def is_long_word(word):
    return len(word) > 5

words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(is_long_word, words))
print(long_words)
