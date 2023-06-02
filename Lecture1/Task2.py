# Задача 2: Найдите сумму цифр трехзначного числа.
n = input("Введите трехзначное число: ")

if len(n) != 3:
    print("Это не трехзначное число!")
else:
    digits = [int(digit) for digit in n]
    print("Сумма цифр числа:", sum(digits))
