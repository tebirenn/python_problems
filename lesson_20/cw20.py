import re

# #---------- Easy A ----------#

# text = input()

# res = re.sub(r"\d", "", text)   # Заменяем цифру на пустую строку

# print(res)





# #---------- Easy B ----------#

# text = input()

# res = re.split(r"[\s.,]", text) # Разделяем через пробел, точку или через запятую(Чтобы паттерн обозначил только одного из них, нужно указать набором)

# print(res)





# #---------- Easy C ----------#

# text = input()

# # Через спец. символ "^" проверяем начало строки
# # И чтобы не зависить от регистра, ставим IGNORECASE
# if re.search(r"^the", text, flags=re.IGNORECASE):
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")





# #---------- Medium A ----------#

# text = input()
# res = re.search('decode', text, flags=re.IGNORECASE)    # Ищем слово decode 

# if res:                         # Если переменная res не пуста
#     print(*res.span())          # Выводим индексы найденного слова 
# else:
#     print("Совпадений нет!")    # Иначе слово не найдено





# #---------- Medium B ----------#

# link = input()
# patt = r"^https?://[a-z]+\.[a-z]+/?$"   # Составляем паттерн по задаче 

# print(bool(re.search(patt, link)))      # Выводим ответ в типе bool





# #---------- Medium C ----------#

# text = input()

# res = re.findall(r"\b[A-Z][a-z]+\b", text)  # Составим паттерн по задаче и находим всё что соответствует

# print(res)





# #---------- Hard A ----------#

# email = input("email: ")
# patt = r"^[a-z0-9_.]+@[a-z]{2,6}\.[a-z]{2,4}$"      # Составим паттерн по задаче

# if re.search(patt, email):                          # Проверяем email по паттерну
#     print("send me meme")
# else:
#     print("uh?")





#---------- Hard B ----------#

phone_number = re.sub(r"\D", "", input())   # Принимаем строку с консоли, и убираем всё что не является цифрой
patt = r"^[78]?(7\d{2})(\d{3})(\d{2})(\d{2})$"  # Составляем паттерн номера, группируя отдельные части 

res = re.search(patt, phone_number)         # Сохраняем результат поиска

if res:                                     # Если поиск успешен, то нормализируем строку
    ans = f"+7 ({res.group(1)}) {res.group(2)} {res.group(3)}-{res.group(4)}"
    print(ans)
else:                                       # Иначе отвечаем что не понимаем 
    print("What is this?")
