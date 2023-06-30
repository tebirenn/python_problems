

#---------- Easy A ----------#

# Создаем двумерный список
res = [
    [1, 5, 9],
    [8, 5, 2],
    [3, 6, 7]
]

# Выводим результат
print(res) 





#---------- Easy B ----------#

# Создаем список
res = []

for i in range(2):      # Создаем цикл который сработает 2 раза
    row = list(map(int, input().split()))       # Принимаем одномерный список
    res.append(row)                             # Добавляем его в общий

print(res)      # Выводим результат





#---------- Easy C ----------#

size = int(input("Размер: "))       # Принимаем размер списка
two_d_list = []                     # Создаем список 

for i in range(size):               # Список на size раз
    row = list(map(int, input().split()))       # Принимаем одномерный список
    two_d_list.append(row)                      # Добавляем его в общий

negative_cnt = 0                    # Счетчик для отрицательных чисел

for row in two_d_list:              # Итерируем двумерный список
    for el in row:                  # Итерируем элементы дорожки
        if el < 0:                  # Если элемент ниже нуля
            negative_cnt += 1       # +1 в количество

print(f"Количество отрицательных элементов: {negative_cnt}")





#---------- Easy D ----------#

n, m = map(int, input().split())    # Принимаем два числа
two_d_list = []                     # Создаем список 

for i in range(n):                  # Список на n раз
    row = list(map(int, input().split()))       # Принимаем одномерный список
    two_d_list.append(row)                      # Добавляем его в общий

print() # Для отступа

for row in two_d_list:              # Итерируем двумерный список
    print(row[::-1])                # Выводим каждую дорожку предварительно отзеркалив





#---------- Medium A ----------#

n, m = map(int, input().split())    # Принимаем два числа
two_d_list = []                     # Создаем список 

for i in range(n):                  # Список на n раз
    row = list(map(int, input().split()))       # Принимаем одномерный список
    two_d_list.append(row)                      # Добавляем его в общий

for i in range(n):                  # Итерируем двумерный список по индексам
    for j in range(m):
        if (i + j) % 2 == 0:        # Если сумма индексов четная
            two_d_list[i][j] += 1   # К элементу с данным индексами прибавляем 1
        else:
            two_d_list[i][j] += 1   # Иначе вычитаем 1

print() # Для отступа

for row in two_d_list:              # Выводим конечный список
    print(*row)





#---------- Medium B ----------#

n, m = map(int, input().split())    # Принимаем два числа
two_d_list = []                     # Создаем список 

for i in range(n):                  # Список на n раз
    row = list(map(int, input().split()))       # Принимаем одномерный список
    two_d_list.append(row)                      # Добавляем его в общий

max_el = two_d_list[0][0]
for row in two_d_list:              # Итерируем каждый элемент двумерного списка
    for el in row:
        if el > max_el:             # Если находим элемент больше чем max_el
            max_el = el             # Меняем значение max_el на данный элемент

for i in range(n):                  # Итерируем двумерный список по индексам
    for j in range(m):
        if two_d_list[i][j] == max_el:  # Если некий элемент равен к максимальному
            print(i, j, sep=" : ")      # Выводим данные индексы





#---------- Medium C ----------#

size = 8                            # Переменная где будет храниться размер
desk = []                           # Создаем список

for i in range(size):               # Список на size раз
    row = list(input())             # Принимаем одномерный список из символов
    desk.append(row)                # Добавляем его в общий

for i in range(size):               # Итерируем двумерный список по индексам
    for j in range(size):

        if desk[i][j] == "X":       # Если мы нашли элемент X
            desk[i][j] = "@"        # Этот элемент меняем на @ и далее нужно поменять элементы рядом
            if i-1 >= 0:            # Но каждый раз нужно проверять что -1 не уйдет в минус и +1 не выйдет за границы  
                desk[i-1][j] = "@"
            if i+1 < size:
                desk[i+1][j] = "@"
            if j-1 >= 0:
                desk[i][j-1] = "@"
            if j+1 < size:
                desk[i][j+1] = "@"

print() # Для отступа

for row in desk:                    # Выводим двумерный список
    print(*row, sep="")





#---------- Hard A ----------#

size = 8                            # Переменная где будет храниться размер
desk = []                           # Создаем список

for i in range(size):               # Список на size раз
    row = list(input())             # Принимаем одномерный список из символов
    desk.append(row)                # Добавляем его в общий

# Надо найти ладью
for i in range(size):               # Итерируем список по индексам
    for j in range(size):
        if desk[i][j] == "R":       # Если нашли ладью
            ri = i                  # Сохраняем его индексы
            rj = j

# Ладья ходит по вертикали и горизонтали
# Запускаем 4 цикл в 4 стороны и начинаем по пути менять элементы на !
for i in range(ri-1, -1, -1):       # В минус до нуля по вертикали
    desk[i][rj] = "!"
for i in range(ri+1, size):         # В плюс до size по вертикали
    desk[i][rj] = "!"

for j in range(rj-1, -1, -1):       # В минус до нуля по горизонтали
    desk[ri][j] = "!"
for j in range(rj+1, size):         # В плюс до size по горизонтали
    desk[ri][j] = "!"

print() # Для отступа

for row in desk:                    # Выводим двумерный список
    print(*row, sep="")





#---------- Hard B ----------#

size = 8                            # Переменная где будет храниться размер
desk = []                           # Создаем список

for i in range(size):               # Список на size раз
    row = list(input())             # Принимаем одномерный список из символов
    desk.append(row)                # Добавляем его в общий

# Надо найти слона
for i in range(size):               # Итерируем список по индексам
    for j in range(size):
        if desk[i][j] == "S":       # Если нашли слона
            si = i                  # Сохраняем его индексы
            sj = j

                                    # Слон ходит по диагонали
i, j = si-1, sj-1                   # Далее нужно запустить 4 цикла в 4 диагонали
while i >= 0 and j >= 0:            # Индексы будут идти иногда в плюс, иногда в микус
    desk[i][j] = "!"                # Главное поставить условие чтобы они не вышли за границу 
    i -= 1                          # И по пути продвижения цикла, элементы будут меняться на !
    j -= 1

i, j = si-1, sj+1
while i >= 0 and j < size:
    desk[i][j] = "!"
    i -= 1
    j += 1

i, j = si+1, sj-1
while i < size and j >= 0:
    desk[i][j] = "!"
    i += 1
    j -= 1

i, j = si+1, sj+1
while i < size and j < size:
    desk[i][j] = "!"
    i += 1
    j += 1

print() # Для отступа

for row in desk:                    # Выводим двумерный список
    print(*row, sep="")





#---------- Hard C ----------#

size = 8                            # Переменная где будет храниться размер
desk = []                           # Создаем список

for i in range(size):               # Список на size раз
    row = list(input())             # Принимаем одномерный список из символов
    desk.append(row)                # Добавляем его в общий

# Надо найти коня
for i in range(size):               # Итерируем список по индексам
    for j in range(size):
        if desk[i][j] == "K":       # Если нашли коня
            ki = i                  # Сохраняем его индексы
            kj = j

# Конь ходит по букву Г(два шага по вертикали/горизонтали) и один шаг в другую сторону перпендикулярно
if (ki-2) >= 0 and (kj-1) >= 0:       # Опять же смотрим после наших арифметичиских операций не выйдет ли индекс за рамки
    desk[ki-2][kj-1] = "!"            # Там где минусуем нужно проверить чтобы было больше/равно к нулю, а там где + чтобы было ниже size
if (ki-2) >= 0 and (kj+1) < size:     # Если проверка проходит данную позицию меняем на !
    desk[ki-2][kj+1] = "!"
if (ki+2) < size and (kj-1) >= 0:
    desk[ki+2][kj-1] = "!"
if (ki+2) < size and (kj+1) < size:
    desk[ki+2][kj+1] = "!"
if (ki-1) >= 0 and (kj-2) >= 0:
    desk[ki-1][kj-2] = "!"
if (ki+1) < size and (kj-2) >= 0:
    desk[ki+1][kj-2] = "!"
if (ki-1) >= 0 and (kj+2) < size:
    desk[ki-1][kj+2] = "!"
if (ki+1) < size and (kj+2) < size:
    desk[ki+1][kj+2] = "!"

print() # Для отступа

for row in desk:                    # Выводим двумерный список
    print(*row, sep="")