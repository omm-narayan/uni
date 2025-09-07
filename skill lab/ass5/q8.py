t = (1, 2, 3, 4)
print("Original tuple:", t)

l = list(t)
l[1] = 4
t = tuple(l)

print("Modified tuple:", t)
