# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def cm_elements(n, m):
    print("Введите элементы первого множества:")
    set1 = set()
    for i in range(n):
        set1.add(int(input()))

    print("Введите элементы второго множества:")
    set2 = set()
    for i in range(m):
        set2.add(int(input()))

    common_elements = sorted(set1 & set2)
    print("Общие элементы, выведенные в порядке возрастания:")
    for element in common_elements:
        print(element)


# Запрос данных у пользователя и вызов функции
n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))
cm_elements(n, m)
