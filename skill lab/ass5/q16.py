vowels = set('aeiouAEIOU')
sentence = input("Enter a sentence: ")
result = ''.join('*' if c in vowels else c for c in sentence)
print(result)
