



#---------- Easy A ----------#

from math import sqrt   # Нам нужен функция квадратного корня

a = int(input("a: "))
b = int(input("b: "))

for num in range(a, b+1):         # Рассматриваем все числа от a до b

    sqrt_num = sqrt(num)          # Вычислаяем квадратный корень числа 
    # Если число полный квадрат, то его корень должен получиться целым числом
    if sqrt_num == int(sqrt_num): # Проверка на целосность числа 
        print(num, end=" ")




#---------- Easy B ----------#

num  = int(input("Число: "))

print("Делители числа", num, end=":\n")

for div in range(1, num+1):       # Рассматриваем все числа от 1 по num
    if num % div == 0:            # Проверяем делиться ли num на div
        print(div, end=" ")





#---------- Medium A ----------#

n = int(input("Количесто вводимых чисел: "))
is_zero = False                    # Переменная чтобы определить есть ли 0 среди чисел

for i in range(n):                 # Цикл на n раз
    num = int(input())

    if num == 0:
        is_zero = True             # Если заметил 0 среди вводимых чисел is_zero меняем на True


# После цикла нужно проверить поменялся ли is_zero на True
if is_zero:
    print("YES")
else:
    print("NO")




#---------- Medium B ----------#

n = int(input("Количесто вводимых чисел: "))

# Переменные куда подсчитаем положительные/отрицательные/нейтральные числа
cnt_positive = 0
cnt_negative = 0
cnt_neitral = 0

for i in range(n):                 # Цикл на n раз
    num = int(input())

    if num > 0:                    # Положительные числа выше 0
        cnt_positive += 1
    elif num < 0:                  # Отрицательные наоборот, ниже 0
        cnt_negative += 1
    else:                          # Остальные(те кто равны к 0) будут нейтральны
        cnt_neitral += 1

print("Количество нулей", cnt_neitral)
print("Количество положительных", cnt_positive)
print("Количество отрицательных", cnt_negative)






#---------- Hard A ----------# 

n = int(input("Высота лесенки: "))
res = ""

for i in range(1, n+1):         # Цикл от 1 по n
    res = res + str(i)          # Все числа постепенно добавляются в конец строки RES
    print(res)                  # Тем самым печатая каждый раз RES, получаем лесенку



#---------- Hard B ----------#

n = int(input("Количество карт: "))

all_sum = 0           # Сумма всех возможных карточек
for card in range(1, n+1):
    all_sum += card

have_sum = 0          # Сумма карточек которых мы имеем
for i in range(n-1):  # Цикл запускается на 1 круг меньше чем n, потому что одной карточки не будет
    card = int(input())
    have_sum += card

# Отняв из всей суммы, сумму которую мы имеем, мы получим ту карту котоый не достает
lost_card = all_sum - have_sum
print("Потерянная карта: ", lost_card)