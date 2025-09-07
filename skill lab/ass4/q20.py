input_list = [1, 7, 3, 6, 5, 6]
found_index = -1

for i in range(len(input_list)):
    left_sum = sum(input_list[:i])

    right_sum = sum(input_list[i+1:])

    if left_sum == right_sum:
        found_index = i
        break

print("Input list:", input_list)

if found_index != -1:
    print("Equilibrium index found at:", found_index)
else:
    print("No equilibrium index found.")
