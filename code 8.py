text = input("Nhập một câu: ")

# Biến đếm chữ hoa
upper_count = 0

# Biến đếm chữ thường
lower_count = 0

# Duyệt từng ký tự
for char in text:

    # Nếu là chữ hoa
    if char.isupper():
        upper_count += 1

    # Nếu là chữ thường
    elif char.islower():
        lower_count += 1

print("Số chữ hoa:", upper_count)
print("Số chữ thường:", lower_count)