import math

result = []

# Duyệt từ 100 đến 2000
for n in range(100, 2001):

    # Tìm căn bậc hai nguyên
    root = math.isqrt(n)

    # Kiểm tra n có phải số chính phương không
    if root * root == n:

        # Biến đếm số chữ số chẵn
        even_count = 0

        # Duyệt từng chữ số của n
        for digit in str(n):

            # Kiểm tra chữ số có chẵn không
            if int(digit) % 2 == 0:
                even_count += 1

        # Phải có ít nhất 2 chữ số chẵn
        if even_count >= 2:
            result.append(str(n))

# In kết quả cách nhau bởi dấu phẩy
print(",".join(result))