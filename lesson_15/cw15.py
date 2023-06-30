#---------- Easy A ----------#

def simple() -> None:
    print("Hi there, Im using WhatsApp")

simple() # Вызов функций





#---------- Easy B ----------#

def show_age(age: int) -> None:     # Принимает один аргумент age(int). Ничего не возвращает
    print(f"I'm {age} years old.")

n = int(input())
show_age(n) # Вызываем функцию, в качестве аргумента age передаем n который принимался с консоли





#---------- Easy C ----------#

def is_even(number: int) -> bool:   # Принимаем один аргумент number(int), возвращает bool значение
    return number % 2 == 0

num = int(input("number: "))

# При вызове функций передаем num в качестве аргунта number
if is_even(num):                    # Функция возвращает True или False. Можно это использовать для условия                  
    print("even")                   # Функция возвращает True если число четное
else:
    print("odd")                    # Иначе сработает else. Число нечетное





#---------- Easy D ----------#

def sum_one_to_n(number: int) -> int:   # Принимает один аргумент number(int), возвращает сумму(int)
    res_sum = 0                         # Переменная куда будет всё суммироваться

    for i in range(1, number+1):        # Цикл от 1 по number
        res_sum += 1                    # Всё складываем в res_sum

    return res_sum                      # После завершения цикла возвращаем res_sum

num = int(input())
print(sum_one_to_n(num))                # Передаем num(принимается с консоли), и выводим то что возвращает функция





#---------- Medium A ----------#

def have_digit(text: str) -> bool:      # Функция принимает один str, возвращает bool значение

    for symbol in text:                 # Итерируется строка
        if symbol.isdigit():            # Проверка является ли символ числовым
            return True                 # Если да завершаем функцию и даем ответ True
        
    return False                        # Если до этого момента функция не завершилась, значит число не было найдено, выдаем False


s = input()

if have_digit(s):                       # Если строка имеет числовой символ
    print("cool")
else:
    print("hot")





#---------- Medium B ----------#

def is_prime(number: int) -> bool:      # Функция должен получить одно целое число, возвращает bool значение

    if number < 2:                      # Всё что ниже 2, не может быть простым
        return False                    # Если так, завершаем функцию возвращяя False
    
                                        # Если всё таки число больше/равно 2
    for i in range(2, number):          # Создаем цикл от 2 до самого числа
        if number % i == 0:             # Если наше число будет хоть на одну из них делиться
            return False                # То это число не может быть простым, завершаем функцию возвращяя False
        
    return True                         # Если функция не завершилась в двух пред. return-ах, значит число прошел проверку, True

num = int(input())
print(is_prime(num))                    # Передаем num(принимается с консоли), и выводим то что возвращает функция





#---------- Medium C ----------#

def sum_of_digits(number: int) -> int:  # Принимает один аргумент number(int), возвращает сумму(int)
    # Этот алгоритм ранее был использован в пятом уроке
    res_sum = 0
    number = abs(number)

    while number >= 0:
        res_sum += number % 10
        number //= 10

    return res_sum                      # Возвращаем сумму


num = int(input())
print(sum_of_digits(num))               # Передаем num(принимается с консоли), и выводим то что возвращает функция





#---------- Hard A ----------#

def my_sort(numbers: list) -> list:     # Принимает список, возвращает список(отсортированный)
    evens = []                          # Создается два списка(для четных и нечетных)
    odds = []

    for el in sorted(numbers):          # Итерируем отсортированный список
        if is_even(el):                 # Проверяем элемент четный ли
            evens.append(el)            # Если да то эл. добавляет в список четных
        else:
            odds.append(el)             # Иначе в список нечетных

    return evens + odds


nums = list(map(int, input().split()))  # Принимаем список
print(*my_sort(nums))                   # Передаем в функцию список, и выводим тот список которую функция возвращает
    




#---------- Hard B ----------#

def k_max(foo: list, k: int):
    foo = set(foo)          # Переводим в сет чтобы избавиться от дубликатов
    foo = sorted(foo)       # Сортируем

    return foo[-k]          # Выводим k-тый элемент с конца(потому что после сортировки, максимальные элементы в конце)
    
nums = input().split()      # Принимаем список
k = int(input())
print(k_max(nums, k))





#---------- Hard C ----------#

def only_digit(text: str) -> str:       # Функция принимает строку, возвращает ответ ввиде строки
    digit_cnt = 0                       # Переменная куда будем считать количество чисел в строке

    for symbol in text:                 # Итерируем строку
        if symbol.isdigit():            # Если символ числовой
            digit_cnt += 1              # То в количество +1

    if digit_cnt == len(text):          # Если количество чисел и длина строки равны, то строка полностью состоит из цифр
        return "very good"
    elif digit_cnt == 0:                # Иначе-если количество == 0, то в строке нет цифр
        return "so bad"
    else:                               # Иначе всё в перемешку
        return "not bad"          


s = input()
print(only_digit(s))                    # Выводим ответ функций, которая получила в качестве аргумента s(с консоли)      
