import random

N = int(input("Введите количество элементов в массиве: "))
A = [random.randint(1, 10) for _ in range(N)]
X = int(input("Введите число X: "))

count = 0
for num in A:
    if num == X:
        count += 1
print(f"{A}")
print(f"Число {X} встречается {count} раз(а) в массиве.")
