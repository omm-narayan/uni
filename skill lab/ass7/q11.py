from functools import reduce

def product(x, y):
    return x * y

numbers = [1, 2, 3, 4]
result = reduce(product, numbers)
print(result)
