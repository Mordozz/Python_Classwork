S = int(input("Сумма: "))
P = int(input("Производная двух чисел: "))
found = False

for X in range(1, 1001):
    if found:
        break
    for Y in range(1, 1001):
        if X + Y == S and X * Y == P:
            print(f"Числа: {X} и {Y}")
            found = True
            break
if not found:
    print("Невозможно найти такие числа.")
