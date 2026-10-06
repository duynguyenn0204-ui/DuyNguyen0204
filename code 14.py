d = {}

while True:
    print("\n1.Thêm  2.Tra  3.Xóa  0.Thoát")
    ch = input("Chọn: ")

    if ch == "1":
        en = input("English: ")
        vi = input("Vietnamese: ")
        d[en] = vi

    elif ch == "2":
        en = input("Từ cần tra: ")
        print(d.get(en, "Không tìm thấy"))

    elif ch == "3":
        en = input("Từ cần xóa: ")
        d.pop(en, None)

    elif ch == "0":
        break