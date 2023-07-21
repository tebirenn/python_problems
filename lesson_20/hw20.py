import re

#---------- Easy A ----------#

date_time = input()

res = re.search(r"([0-9]{4})/[0-9]{2}/[0-9]{2}", date_time) # Группируем год
year = int(res.group(1))    # Достаем год из результата

if 1000 <= year <= 2012:    # Проверяем год
    print("Yes")
else:
    print("No")





#---------- Medium A ----------#

text = input()

# Всё что находиться между двумя А группируем, используя при замене, но сбоку от него будет "!"
res = re.sub(r"\ba([^a]+)a\b", r"!\1!", text, flags=re.IGNORECASE)

print(res)





#---------- Medium B ----------#

text = input()
letter = input()

words = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)    # Находим все слова
cnt = 0                                                     # Для количества слов

for word in words:                                          # Итерируем все слова
    if re.search(letter, word, flags=re.IGNORECASE):        # Если в слове есть данная буква
        cnt += 1                                            # увеличиваем cnt на 1

print(cnt)  # Выводим ответ





#---------- Hard A ----------#

phone_number = re.sub(r"\D", "", input())   # Принимаем строку с консоли, и убираем всё что не является цифрой

patt = r"^(7|8)7(0|4)7\d{7}$"               # Составляем паттерн чтобы код был только 707 или 747

if re.search(patt, phone_number):           # Если подходит по паттерну
    print("Hello?")                         # Берем трубку
else:
    print("Declined")                       # Иначе нет