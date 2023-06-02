import random

N = int(input("Введите количество элементов в массиве: "))
A = [random.randint(1, 100) for _ in range(N)]
X = int(input("Введите число X: "))

closest_element = A[0]
min_difference = abs(A[0] - X)

for num in A:
    difference = abs(num - X)
    if difference < min_difference:
        min_difference = difference
        closest_element = num
print(f"{A}")
print(f"Самый близкий элемент к числу {X} в массиве: {closest_element} ")
