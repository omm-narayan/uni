print("Numbers between 1 and 10000 divisible by the sum of their digits:\n")

for num in range(1, 10001):
    sum_of_digits = sum(int(digit) for digit in str(num))
    if num % sum_of_digits == 0:
        print(num, end=" ")