


### Easy A ###

for i in range(5, 16):   # Цикл от 5 по 15
    if i == 10:          # Если 10 то пропускаем
        continue

    print(i, end=" ")    # А остальные числа будут напечатаны


### Easy B ###

n = int(input("n: "))

# Цикл от 1 по n
for i in range(1, n+1):  # n+1 чтобы само число n входил в отрезок
    print(i, end=" ")



### Easy C ###

l = int(input("L: "))
r = int(input("R: "))

# Цикл от L по R
for i in range(l, r+1):  # r+1 по той же причине как в Easy B 
    if i % 2 == 0:       # Проверка на четность числа i
        print(i, end=" ")



### Easy D ###

l = int(input("L: "))
r = int(input("R: "))

# Цикл от L по R (L больше чем R, изза этого шаг нужен отрицательный)
for i in range(l, r-1, -1):     # r-1 чтобы r был включительным в отрезке
    if i % 2 != 0:              # Проверка на нечетность числа i
        print(i, end=" ")



### Medium A ###

text = input("string: ")      # Принимаем строку

for symbol in text:           # Итерация по строке 
    print(symbol, end=" ")    # Вывод каждого символа через пробел




### Medium B ###

a = int(input("a: "))
b = int(input("b: "))

result = 0              # Сюда будем складывать все числа от a по b

# цикл от a по b
for i in range(a, b+1):
    result += i   # Складываем все числа i в result

print("Сумма:", result)




### Medium C ###

a = int(input("a: "))
b = int(input("b: "))


# возможный минимальный НОК это 1
# а возможный максимальный НОК это их умножение
for nok in range(1, a*b+1):             # Рассматриваем все возможные НОК
    if nok % a == 0 and nok % b == 0:   # Если рассмартиваемое число и на a и на b делиться
        print("НОК:", nok)              # То мы нашли его
        break                           # Дальше нет смылса продолжать цикл раз уж нашли




### Hard A ###

num = int(input("Number: "))

if num < 2:          # Все числа ниже 2 не подходят
    print("Common")
else:
    # А остальные числа нужно проверить

    cnt = 0      # Сюда будем считать количество делителей числа

    for i in range(1, num+1):   # Все числа от 1 по num
        if num % i == 0:        # Если num делится на какие то числа в отрезке
            cnt += 1            # +1 в количество делителей


    # У простых чисел только два делителя(1 и само число)
    if cnt == 2:     
        print("Prime")
    else:
        print("Common")


    

### Hard B ###

n = int(input("Количество букв: "))
result = 0                          # Сюда будем суммировать 

for i in range(n):                  # Цикл на n раз
    letter = input()                # Буква с консоли

    if "a" <= letter <= "z":        # Проверка строчная ли буква
        # Через ord узнаем код буквы
        result += ord(letter) - 96  # У маленьких букв если отнять 96
                                    # Можно узнать порядок в алфавите 
    else:                           # Иначе это большая буква
        result += ord(letter) - 64  # У больших букв это число 64


print("Сумма:", result)





### Hard C ###

a = int(input("a: "))
b = int(input("b: "))
x = int(input("x: "))

for num in range(a, b+1):     # Цикл от a по b

    summa = 0               # Тут будет сумма цифр числа 
    num_copy = num          # Копия числа num
    num = abs(num)          # Избавляем от знака "-" у отрицательных чисел

    # Этот алгоритм действий был ранее описан в Lesson 5
    while num != 0:
        summa += num % 10
        num //= 10

    if summa == x:          # Если сумма цикл равна к специальной числе x
        print(num_copy)     # Копия числа нужна на этом моменте 
                            # Потому что само число num уже стало нулём
                     
