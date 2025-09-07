nested_list = [[1, 2], [3, 4], [5, 6]]

flattened_list = [item for sublist in nested_list for item in sublist]

print("Original nested list:", nested_list)
print("Flattened list:", flattened_list)
