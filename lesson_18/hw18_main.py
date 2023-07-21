#---------- Easy A ----------#

from math import sqrt

a = int(input("a="))
b = int(input("b="))

print((sqrt(a) - sqrt(b))**2)





#---------- Easy B ----------#

from math import tan, pi

a = int(input("a="))
b = int(input("b="))

print(tan(-a * pi / b))





#---------- Medium A ----------#

from random import randint                      # randint Для случайных чисел
from hw18_module import sum_of_digits           # sum_of_digits Для суммы цифр в числе 

num = randint(1000, 9999)                       # Выбираем случайное 4ех значное число
print(f"num={num}, sum={sum_of_digits(num)}")   # Выводим ответ используя функцию из нашего модуля





#---------- Medium B ----------#

from hw18_module import my_abs, my_pow, my_sqrt

# Импортируем созданные функций и показываем их работоспособность 
print(my_abs(-9))
print(my_sqrt(50))
print(my_pow(2, 5))





#---------- Hard A ----------#

from random import choice               # Функция choice выбирает один случайный элемент из коллекций 

my_list = [45, 2, 65, 789, -66, 21 -3]  # Создаем некий список
max_el = max(my_list)                   # Вычисляем максимальный из них
cnt = 0                                 # Для количества попыток

while True:                             # Цикл бесконечный пока цель не достигнута
    rand_el = choice(my_list)           # Выбираем случайный элемент из списка
    cnt += 1                            # Одна попытка сделана
    print(f"Попытка #{cnt}: Элемент={rand_el}")     # Показываем пользователю что произошло

    if rand_el == max_el:               # Если случайный элемент это максимальный, то мы достигли цели
        break
    

