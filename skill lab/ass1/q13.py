subject1 = float(input("Enter marks in subject 1: "))
subject2 = float(input("Enter marks in subject 2: "))
subject3 = float(input("Enter marks in subject 3: "))
subject4 = float(input("Enter marks in subject 4: "))

total_marks = subject1 + subject2 + subject3 + subject4
percentage = (total_marks / 400) * 100

print(f"Percentage = {percentage:.2f}%")
