# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def stpn(A, B):
    if B == 0:
        return 1
    elif B < 0:
        return 1 / stpn(A, -B)
    else:
        return A * stpn(A, B - 1)

A = int(input("Введите число: "))
B = int(input("Введите степень числа: "))

result = stpn(A, B)
print("Вывод:", result)
