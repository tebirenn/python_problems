import re

#---------- Easy A ----------#

text = input()

print(bool(re.search(r"\d", text))) # Проверка есть ли какая то цифра внутри строки





#---------- Easy B ----------#

text = input()

# Строка от начала до конца должен состоять из символов в наборе
if re.search(r"^[a-zA-Z0-9]+$", text):      
    print("Нашел совпадение!")
else:
    print("Не нашел совпадение!")





#---------- Easy C ----------#

text = input()

# В строке должна быть большая буква затем маленькая
if re.search(r"[A-Z][a-z]", text):      
    print("Нашел совпадение!")
else:
    print("Не нашел совпадение!")





#---------- Medium A ----------#

text = input()

# В строке должна заканчиваться на cool
if re.search(r"cool$", text):      
    print("Нашел совпадение!")
else:
    print("Не нашел совпадение!")





#---------- Medium B ----------#

text = input()

# В строке должна начинаться на a
# заканчиваться на b
# Между ними что угодно сделано через спец символ "."
if re.search(r"^a.+b$", text):      
    print("Нашел совпадение!")
else:
    print("Не нашел совпадение!")





#---------- Medium C ----------#

text = input()

# Паттерн составлен по описаний в задаче 
patt = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
if re.search(patt, text):      
    print("IP")
else:
    print("Something else")





#---------- Hard A ----------#

text = input()

# Паттерн составлен по описаний в задаче 
patt = r'^(7|8)7[0-9]{9}$'
if re.search(patt, text):      
    print("Call me maybe")
else:
    print("Something else")





#---------- Hard B ----------#

ip = input()

# В начале одного числа может быть 1 или 2 нуля, 3ьи ноль нам уже будет нужен
# Так что все кроме 1 и 2 нуля береться в скобки, и ставиться обратно на место при замене
new_ip = re.sub(r'\b0{1,2}(\d{1,3})\b', r'\1', ip)

print(new_ip)