#---------- Easy A ----------#

var = [13, 4, 7, 5, 6, 9]

#---------- Easy B ----------#

student = {
    'name': 'Aidana',
    'age': 21,
    'gpa': 3.88
}


#---------- Medium A ----------#

def str_reverse(string: str) -> str:
    return string[::-1]                 # С помощью среза, реверсируем строку

#---------- Hard A ----------#

def sum_of_max_min(nums: list) -> int|float:
    max_el = max(nums)          # Максимальный элемент из списка
    min_el = min(nums)          # Минимальный элемент из списка
    
    return max_el + min_el      # Сумма максимума и минимума

#---------- Hard B ----------#

def count_of_letters(string: str) -> dict:
    res = dict.fromkeys(string)     # Создаем словарь из ключей от строки, у всех значение будет 0

    for letter in string:           # Итерируем строку
        res[letter] += 1            # Каждому символу в строке к значению прибавляем 1

    return res                      # Возвращаем результат