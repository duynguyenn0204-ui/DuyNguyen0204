text = input("Nhập chuỗi: ")

# Tách chuỗi thành từng từ
# Đồng thời loại bỏ khoảng trắng dư thừa
words = text.split()

# Danh sách kết quả
result = []

# Duyệt từng từ
for word in words:

    # Viết hoa chữ cái đầu,
    # các chữ còn lại chuyển thành chữ thường
    word = word.capitalize()

    # Thêm vào danh sách
    result.append(word)

# Ghép các từ bằng đúng 1 khoảng trắng
text = " ".join(result)

print("Chuỗi sau khi chuẩn hóa:")
print(text)