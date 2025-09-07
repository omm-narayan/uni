from functools import reduce

def concat(x, y):
    return x + y

strings = ["Hello", " ", "World", "!"]
result = reduce(concat, strings)
print(result)
