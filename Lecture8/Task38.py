def read_phonebook():
    with open('phonebook.txt', 'r') as file:
        phonebook = [line.strip().split(',') for line in file]
    return phonebook

def write_phonebook(phonebook):
    with open('phonebook.txt', 'w') as file:
        for entry in phonebook:
            file.write(','.join(entry) + '\n')

def print_phonebook(phonebook):
    for row in phonebook:
        print(', '.join(row))

def find_entry(phonebook, name):
    for i, row in enumerate(phonebook):
        if name in row[0:2]:
            return i
    return -1

def edit_entry(phonebook):
    name = input("Введите имя или фамилию для редактирования: ")
    index = find_entry(phonebook, name)
    if index != -1:
        print("Текущая запись: ")
        print(', '.join(phonebook[index]))
        phonebook[index] = input("Введите новую запись в формате 'Фамилия,Имя,Номер,Описание': ").split(',')
        write_phonebook(phonebook)
    else:
        print("Запись не найдена.")

def delete_entry(phonebook):
    name = input("Введите имя или фамилию для удаления: ")
    index = find_entry(phonebook, name)
    if index != -1:
        del phonebook[index]
        write_phonebook(phonebook)
    else:
        print("Запись не найдена.")

phonebook = read_phonebook()

while True:
    print("\nТелефонный справочник: ")
    print_phonebook(phonebook)
    print("\nВведите команду (редактировать, удалить, выход): ")
    command = input()
    if command == "редактировать":
        edit_entry(phonebook)
    elif command == "удалить":
        delete_entry(phonebook)
    elif command == "выход":
        break
