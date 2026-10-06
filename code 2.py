from datetime import date

day = int(input("Nhập ngày sinh: "))
month = int(input("Nhập tháng sinh: "))
year = int(input("Nhập năm sinh: "))

today = date.today()

age = today.year - year

if (today.month, today.day) < (month, day):
    age -= 1

print("Tuổi của bạn là:", age)