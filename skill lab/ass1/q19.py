basic_salary = float(input("Enter basic salary: "))

da = 0.60 * basic_salary  # 60% of basic
hra = 0.15 * basic_salary  # 15% of basic
gross_salary = basic_salary + da + hra

print(f"Basic Salary = {basic_salary}")
print(f"DA (60%) = {da}")
print(f"HRA (15%) = {hra}")
print(f"Gross Salary = {gross_salary}")
