num = int(input("Enter a number: "))
original_num = num
num_digits = len(str(num))
sum_of_powers = 0
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num = num // 10
if original_num == sum_of_powers:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")