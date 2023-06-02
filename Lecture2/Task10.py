import random

n = int(input("Введите кол-во монеток: "))
coins = [random.randint(0, 1) for orient in range(n)]

print("Состояние монеток: ", coins)

tails = coins.count(0)
heads = coins.count(1)
flips = min(tails, heads)

print(f"Необходимо перевернуть {flips} монеток")