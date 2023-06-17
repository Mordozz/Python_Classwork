stih = input("Введите стихотворение: ")

glas = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
rth = [sum(word.count(vowel) for vowel in glas) for word in stih.split()]

if all(rth[0] == rth[i] for i in range(1, len(rth))):
    print("Парам пам-пам")
else:
    print("Пам парам")
