t = (100, 200, 300, 400, 500)

if 300 in t:
	idx = t.index(300)
	print(f"Index of 300 in {t} is: {idx}")
else:
	print("300 is not in the tuple")
