sv = []

while True:
    print("\n1.Thêm  2.Xem  3.Điểm>7  4.Tìm  5.Sửa  6.Xóa  0.Thoát")
    ch = input("Chọn: ")

    if ch == "1":
        sv.append({
            "mssv": input("MSSV: "),
            "name": input("Tên: "),
            "score": float(input("Điểm: "))
        })

    elif ch == "2":
        for x in sv:
            print(x)

    elif ch == "3":
        for x in sv:
            if x["score"] > 7:
                print(x)

    elif ch == "4":
        m = input("MSSV: ")
        for x in sv:
            if x["mssv"] == m:
                print(x)

    elif ch == "5":
        m = input("MSSV: ")
        for x in sv:
            if x["mssv"] == m:
                x["score"] = float(input("Điểm mới: "))

    elif ch == "6":
        m = input("MSSV: ")
        sv = [x for x in sv if x["mssv"] != m]

    elif ch == "0":
        break