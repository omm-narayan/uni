sentence = "Python is a powerful language"
words = sentence.split()
long_words = [w for w in words if len(w) > 5]
print("Words with more than 5 characters:", long_words)
