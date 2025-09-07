sentence = input("Enter a sentence: ")
words = [w.strip(".,!?;:") for w in sentence.lower().split()]
count_the = sum(1 for w in words if w == 'the')
print(f"Occurrences of 'the' = {count_the}")
