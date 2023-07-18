#---------- Easy A ----------#

my_dict = {"a": 1, "b": 2, "c": 3}      # Создаем словарь
key = input("key: ")                    # Принимаем ключ

try:
    print(my_dict[key])                 # Попытаемся используя данный ключ, вывести значение ключа
except KeyError:
    print("That key does not exist!")   # Если не получиться, обходим исключение, и сообщаем об ошибке 





#---------- Easy B ----------#

num1, num2 = map(int, input().split())  # принимаем два числа

print(num1 if num1 < num2 else num2)    # Находим минимальный из них используя тернарный оператор





#---------- Medium A ----------#

my_list = list(map(int, input().split()))
is_find = False                         # is_find флаг объясняющий нашли ли мы то что нам нужно

for el in my_list:                      # Итерируем список
    if el % 3 == 0 and el % 5 == 0:     # Если элемент делиться и на 3 и на 5
        is_find = True                  # Флаг is_finded меняем на True
        break

if is_find:                             # Если флаг is_find хранит в себе True
    print("Такое число присутствует")   # Число мы нашли 
else:                                   # Иначе нет
    raise Exception("Такое число отсутствует") 





#---------- Medium B ----------#

a = int(input("a: "))                   # Принимаем три числа        
b = int(input("b: "))
c = int(input("c: "))

if a * b == c:                          # Если умножения a и b будет равен к c 
    print(True)                         # Выводим True
else:
    raise Exception(False)              # Иначе вызываем исключение





#---------- Hard A ----------#

a = input("Первое число: ")             # Принимаем три значения
op = input("Ариф. операция")
b = input("Второе число: ")

try:                                
    res = eval(f"{a} {op} {b}")         # Через eval попытаемся вычислить результат операций
    print(res)
except ValueError:                      # Если возникнет ошибка ввода
    print("Ошибка ввода!")              
except ZeroDivisionError:               # Если возникнет ошибка деления на ноль
    print("Ошибка: деление на ноль")
except ArithmeticError:                 # Иная ошибка арифметики
    print("Ошибка арифметики")





#---------- Hard B ----------#

def is_have_three_x(num: int) -> bool:  # Функция получая число возвращает bool
    num = abs(num)                      # Избавляемся от знака -  (Если он есть)

    while num != 0:                     # Алгоритм разбора на числа на части    
        last_digit = num % 10
        num //= 10
        if last_digit % 3 == 0:         # Если некая цифра делиться на 3
            return True                 # возвращаем True
        
    return False                        # Если функция не завершилась до этого момента, возвращаем False


number = int(input("Число: "))          # Принимаем число
print(True if is_have_three_x(number) else False)   # Вывод ответа используя тернарный оператор