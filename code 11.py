balance = 0

with open("Transaction.txt", "r") as f:
    lines = f.readlines()

name = lines[0].replace("Name:", "").strip()

for line in lines[1:]:
    type, money = line.split()
    money = float(money)

    if type == "D":
        balance += money
    else:
        balance -= money * 1.001

with open("BalanceInquiry.txt", "w") as f:
    f.write(f"Name: {name}\nBalance: {balance}")