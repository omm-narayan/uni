s = input("Enter a string: ")
s_letters = [c.lower() for c in s if c.isalpha()]
counts = [(ch, s_letters.count(ch)) for ch in set(s_letters)]

for ch, cnt in sorted(counts):
	print(f"{ch}: {cnt}")
