text = input("Nhập các từ: ")

words = text.split()

words = list(set(words))

words.sort()

result = []

for word in words:
    if word.startswith("A") or word.startswith("a"):
        word = word.upper()

    result.append(word)

print("Kết quả:", " ".join(result))