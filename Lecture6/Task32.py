# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

input_string = input("Введите элементы списка: ")
A = list(map(int, input_string.split()))

min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

result = find_indexes(A, min_value, max_value)
print(result)
