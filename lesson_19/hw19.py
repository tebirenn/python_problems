import re

#---------- Easy A ----------#

text = input()

res = re.findall(r"\d{2}-\d{2}-\d{4}", text)    # Составляем паттерн даты, и ищем всё что соответствует паттерну    
print(res)





#---------- Easy B ----------#

text = input()

# Составляем паттерн слова, и ищем всё что соответствует паттерну    
res = re.findall(r"\b[aeoiuy][a-z]*\b", text, flags=re.IGNORECASE)    
print(res)





#---------- Medium A ----------#

text = input()

# Через $ проверим есть ли цифра в конце
print(bool(re.search(r"\d$", text)))





#---------- Medium B ----------#

text = input()

nums = re.findall(r"\d+", text)     # Находим все числа 

for num in nums:                    # Итерируем числа
    res = re.search(num, text)      # Ищем текущее число из строки
    print(num)                      # Выводим само число
    print("Индекс:", res.start())   # Выводим индекс числа





#---------- Hard A ----------#

text = input()

words = re.findall(r'\b[a-z]{5}\b', text, flags=re.IGNORECASE)  # Ищем слова состоящие из 5 букв

print(words)





#---------- Hard B ----------#

camel_case = input()

# Шаг 1: заменяем большую букву на _большаяБуква  Например: MyFirstName => _My_First_Name
# Шаг 2: срезаем с первого индекса дальше                   _My_Name => My_First_Name
# Шаг 3: заменяем большие буквы на маленькие                My_First_Name => my_first_name
snake_case = re.sub(r"([A-Z])", r"_\1", camel_case)[1:].lower()

print(snake_case)