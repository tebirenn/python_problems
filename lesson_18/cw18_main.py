#---------- Easy A ----------#

from cw18_module import var
print(var[0])                   # Импортируем коллекцию из модуля и выводим нужное значение





#---------- Easy B ----------#

from cw18_module import student

print(student['name'])          # Импортируем коллекцию из модуля и выводим нужное значение
print(student['age'])





#---------- Easy C ----------#

from random import randint

a = int(input("Начало: "))
b = int(input("Конец: "))

print(randint(a, b))            # Случайное число между a и b





#---------- Medium A ----------#

from cw18_module import str_reverse

text = input("строка: ")                    # Принимаем с консоли строку
print("str reversed:", str_reverse(text))   # Выводим перевернутую строку





#---------- Medium B ----------#

from math import sqrt, sin

x = int(input("x="))
y = int(input("y="))

# Собираем формулу как показано на заданий 
res = (sqrt(sin(x) + y**3) + sqrt(x + y)) / (2*x + y)
print(res)





#---------- Medium C ----------#

from math import sin, cos, e

# Собираем формулу как показано на заданий 
res = (sin(5) + 1.75**2) / (3 * e**(cos(7)))

print(res)





#---------- Hard A ----------#

from cw18_module import sum_of_max_min

numbers = list(map(int, input().split()))   # Принимаем список чисел
print(sum_of_max_min(numbers))              # Выводим ответ функций получивший наш список





#---------- Hard B ----------#

from cw18_module import count_of_letters    

text = input("строка: ")            # Принимаем строку
res = count_of_letters(text)        # Сохраняем ответ функций 

for k, v in res.items():            # Выводим информацию из словаря res
    print(f"{k}: {v}")
