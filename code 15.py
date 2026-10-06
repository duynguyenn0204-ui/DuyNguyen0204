r = int(input("Số dòng: "))
c = int(input("Số cột: "))

a = [[int(input(f"a[{i}][{j}]: ")) for j in range(c)] for i in range(r)]

def prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n**0.5) + 1))

print("Tổng số nguyên tố:",
      sum(x for row in a for x in row if prime(x)))

if r == c:
    print("Tổng đường chéo:", sum(a[i][i] for i in range(r)))

mn = min(min(row) for row in a)
mx = max(max(row) for row in a)

print("Min:", mn)
print("Max:", mx)