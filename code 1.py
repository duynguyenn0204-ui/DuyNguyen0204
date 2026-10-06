hours = float(input("Nhập số giờ làm mỗi tuần: "))
rate = float(input("Nhập tiền công mỗi giờ: "))

if hours <= 40:
    salary = hours * rate
else:
    normal_salary = 40 * rate
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * rate * 1.5
    salary = normal_salary + overtime_salary

print("Tiền lương thực lĩnh:", salary)