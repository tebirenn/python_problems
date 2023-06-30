#---------- Easy A ----------#

def power(a, n):    # Функция получает два числа a, b
    return a**n     # Возвращает a в степени b

a, n = int(input()), int(input())
print(power(a, n))  # Выводим ответ вызванной функций, передав два числа





#---------- Easy B ----------#

# Функция получает год(int). Возвращает високосный или нет(bool)
def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True     # True если подходит по условию
    else:
        return False    # Иначе False
    
year = int(input("Год: "))
if is_leap_year(year):  # Если функция дает True получая год
    print("YES")        # То он високосный
else:
    print("NO")         # Иначе нет





#---------- Medium A ----------#

def nok(a: int, b: int) -> int: # Функция получает два числа, и возвращает НОК(int)
    while True:                 # Бесконечный цикл
        reminder = a % b        # Сохраняем остаток

        if reminder == 0:       # Алгоритм должен быть завершен, когда остаток будет 0
            return b            # Возвращается последее состояние второго числа
        
        a = b                   # На протяжений алгоритма, первое число меняется на второе
        b = reminder            # А второе на остаток

x, y = map(int, input().split())
res = nok(x, y)                 # в res сохраняем ответ вызванной функций, которая получила два числа
print(f"НОК: {res}")            # Выводим ответ





#---------- Medium B ----------#

def avg(numbers: list) -> float:
    return sum(numbers) / len(numbers)      # Среднее значение = сумма / количество

nums = list(map(int, input().split()))
print(avg(nums))





#---------- Hard A ----------#

def sum_of_digits(number: int) -> int:  # Принимает один аргумент number(int), возвращает сумму(int)
    # Этот алгоритм ранее был использован в пятом уроке
    res_sum = 0
    number = abs(number)

    while number > 0:
        res_sum += number % 10
        number //= 10

    return res_sum                      # Возвращаем сумму

nums = list(map(int, input().split()))  # Принимаем список чисел
print(*sorted(nums, key=sum_of_digits)) # Сортируем список используя функцию sum_of_digits
                                        # Которая вычислаяет сумму цифр, и выводим отсортированный список





#---------- Hard B ----------#

def reverse_words(sentence: str) -> str:    # Принимаем строку из слов
    words = sentence.split()                # Разделяя слова через split, получаем список из всех слов
    words.reverse()                         # Реверсируем порядок слов
    res = " ".join(words)                   # Собираем все слова в одну строку через пробел с помощью join
    return res 

text = input()                              # Принимается текст
print(reverse_words(text))                  # Выводиться ответ функций получивший наш текст
