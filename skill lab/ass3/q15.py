number = int(input("Enter a number to check its digits: "))
temp_num = number

reference_digit = temp_num % 10

while temp_num > 0:
    if temp_num % 10 != reference_digit:
        print(f"The digits of {number} are not equal.")
        break
    temp_num = temp_num // 10
else:
    print(f"All digits of {number} are equal.")