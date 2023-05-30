



#---------- Easy A ----------#


# Для конвертаций используем функцию eval(), которая может автоматический определять 
length = int(input())  # Бесполезная для решения задачи
x = list(map(eval, input().split()))

print(x)





#---------- Easy B ----------#

length = int(input())  # Бесполезная для решения задачи
numbers = list(map(int, input().split()))   # Вводится список из int

for el in numbers:     # Итерируем список 

    if el % 2 == 1:    # Проверка на нечетность
        print(el, end=" ")




#---------- Medium A ----------#

length = int(input())  # Бесполезная для решения задачи
numbers = list(map(int, input().split()))   # Вводится список из int

max_el = max(numbers)
max_el_index = numbers.index(max_el)       # Индекс максимального элемента находим через метод index()

print(max_el, max_el_index)





#---------- Medium B ----------#

length = int(input())  # Бесполезная для решения задачи
numbers = list(map(int, input().split()))   # Вводится список из int

m = int(input())

ans = numbers.count(m)    # Через метод count находим сколько раз встречается значение m в списке 
print(ans)





#---------- Hard A ----------#

length = int(input())  # Бесполезная для решения задачи
numbers = list(map(int, input().split()))   # Вводится список из int

# Через функций max() и min() находим максимальный и минимальный элемент
max_el = max(numbers)
min_el = min(numbers)

# Через метож index() находим их индексы 
max_index = numbers.index(max_el)
min_index = numbers.index(min_el)

# Делаем swap элементов с помощью индексов
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]


##### *list - распаковка 
print(*numbers)





#---------- Hard B ----------#

numbers = list(map(int, input().split()))   # Вводится список из int
cnt = 0                                     # Для количества пар

# Вложенный цикл чтобы просмотреть все пары
for i in range(0, len(numbers)): 
    for j in range(i+1, len(numbers)):
        # если некие два элемента равны, то они пара
        if  numbers[i] == numbers[j]:
            cnt += 1 # В таком случае добавляем в количество единицу


print("Количество пар:", cnt)