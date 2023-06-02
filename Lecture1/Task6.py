# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.
ticket = input("Введите номер билета: ")
if len(ticket) != 6:
    print("Номер билета должен состоять из 6 цифр!")
else:
    firstHalf = ticket[:3]
    secondHalf = ticket[3:]

    firstHalfDigits = [int(digit) for digit in firstHalf]
    firstHalfDigits = [int(digit) for digit in secondHalf]

    if sum(firstHalfDigits) == sum(firstHalfDigits):
        print("yes")
    else:
        print("no")