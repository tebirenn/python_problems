#---------- Medium A ----------#

def sum_of_digits(number: int) -> int:  # Принимает один аргумент number(int), возвращает сумму(int)
    # Этот алгоритм ранее был использован в пятом уроке
    res_sum = 0
    number = abs(number)

    while number > 0:
        res_sum += number % 10
        number //= 10

    return res_sum                      # Возвращаем сумму

#---------- Medium B ----------#

# Создаем три функций, дубликаты из модуля math
def my_abs(number: int|float) -> int|float:
    return number if number >= 0 else number * (-1)

def my_sqrt(number: int|float) -> float:
    return number**0.5

def my_pow(main: int|float, power: int|float) -> int|float:
    return main**power
