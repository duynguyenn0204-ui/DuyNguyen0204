username = input("Nhập username: ")
password = input("Nhập password: ")


# =========================
# KIỂM TRA USERNAME
# =========================

username_valid = (
    len(username) == 6
    and username.isalnum()
    and username == username.lower()
)


# =========================
# KIỂM TRA PASSWORD
# =========================

# Các ký tự đặc biệt được cho phép
special_chars = "!@#$%^&*"


password_valid = (
    # Độ dài từ 6 đến 12
    6 <= len(password) <= 12

    # Có ít nhất 1 chữ thường
    and any(c.islower() for c in password)

    # Có ít nhất 1 chữ hoa
    and any(c.isupper() for c in password)

    # Có ít nhất 1 chữ số
    and any(c.isdigit() for c in password)

    # Có ít nhất 1 ký tự đặc biệt
    and any(c in special_chars for c in password)
)


# =========================
# IN KẾT QUẢ USERNAME
# =========================

if username_valid:
    print("Username hợp lệ")
else:
    print("Username không hợp lệ")


# =========================
# IN KẾT QUẢ PASSWORD
# =========================

if password_valid:
    print("Password hợp lệ")
else:
    print("Password không hợp lệ")