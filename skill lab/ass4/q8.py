# program to remove duplicates from a list

num = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for item in num:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
