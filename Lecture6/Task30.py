# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

digit = int(input("Введите первый элемент прогрессии: "))
delta = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

progres = [digit + (i - 1) * delta for i in range(1, n + 1)]

print("Значения прогрессии:")
for num in progres:
    print(num)
