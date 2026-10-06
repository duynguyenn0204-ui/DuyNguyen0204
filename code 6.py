data = input("Nhập các số nhị phân: ")

binary_numbers = data.split(",")

result = []

for binary in binary_numbers:
    decimal = int(binary, 2)

    if decimal % 5 == 0:
        result.append(binary)

print(",".join(result))