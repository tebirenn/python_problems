

### Easy A ###

my_list = []   # Cоздали пустой список

for i in range(3):       # Нужно принять три значения, запустим цикл на три раза
    val = input()        # Принимаем значение
    my_list.append(val)  # С помощью метода append() добавим значение в список

print(my_list)




### Easy B ###

# Шаг 1: Через input().split() принимаем список, но все элементы будут в типе str
# Шаг 2: Через функцию map() конвертируем все элементы в тип данных int
# Шаг 3: Через функцию list() конвертируем map объект в список
# Таким образом мы получим список из int
numbers = list(map(int, input().split()))

print(numbers)





### Easy C ###

numbers = list(map(int, input().split()))   # Принимаем список из Int

if len(numbers) == 1:       # Если в списке только один элемент
    print(numbers[0])       # Выводим единственный нулевой элемент
else:
    # Иначе как просилось выводим самый первый и последний по порядку 
    print(numbers[0], numbers[-1])




### Easy D ###

numbers = list(map(int, input().split()))   # Принимаем список из Int
res = sum(numbers) # Вычисляем сумму с помощью функций sum()

print("Сумма элементов списка:", res)





### Medium A ###

numbers = list(map(int, input().split()))   # Принимаем список из Int

for el in numbers:              # Итерируем список
    # Положительное число это число больше нуля 
    if el > 0:
        print(el, end=" ")





### Medium B ###

numbers = list(map(int, input().split()))   # Принимаем список из Int

# Чтобы отсортировать используем метод sort()
# Чтобы сортировка была по убыванию параметр reverse ставим на True
numbers.sort(reverse=True)

# * для распаковки
print(*numbers)





### Medium C ###

numbers = list(map(int, input().split()))   # Принимаем список из Int

ans = max(numbers)       # Максимальный элемент находим через функцию max()
print("Максимальный элемент списка:", ans)






### Hard A ###

numbers = list(map(int, input().split()))   # Принимаем список из Int
spec_number = int(input())                  # Специальное число

for i in range(0, len(numbers)):            # Цикл начинающеся с нуля до конечного индекса
    for j in range(i+1, len(numbers)):      # Цикл начинается с индекса после i до конечного индекса

        # У нас есть два индекса, через них обращаемся к значениям элементов и суммируем их
        # Если сумма получиться равна к специальному числу, выводим два значения
        if numbers[i] + numbers[j] == spec_number:
            print(numbers[i], numbers[j])





### Hard B ###

numbers = list(map(int, input().split()))   # Принимаем список из Int
unique = []                                 # Список для уникальных элементов

for el in numbers:         # Итерация списка numbers 
    # Мы добавляем элемент их numbers, если только его нет в списке unique
    # Таким образом один элемент не будет повторно добавляться 
    if el not in unique:
        unique.append(el)

print(*unique)


### Hard C ###

names = input().split()       # Принимаем список из строк

# Вложенные циклы чтобы перебрать все пары как  Hard A 
for i in range(0, len(names)):
    for j in range(i+1, len(names)): 
        
        # Чем длиннее имя, тем первее в списке он должен стоять
        # Элемент под индексом i первее чем j. Если элемент под индексом i будет по короче по длине, нужно его поменять местами с элементом по длиннее чем он
        if len(names[i]) < len(names[j]):
            names[i], names[j] = names[j], names[i]   # swap

        # Иначе-если длины равны и элемент первее больше чем второй по системе ASCII
        # тоже меняем местами
        elif len(names[i]) == len(names[j]) and names[i] > names[j]:
            names[i], names[j] = names[j], names[i]   # swap
        

# После завершения всех манипуляций, выводим распакованный список
print(*names)