


#---------- Easy A ----------#

# Принимаем две строки 

first = input()
second = input()

# Если они одинаковы
if first == second:
    print("YES")
else:
    print("NO")




#---------- Easy B ----------#

text = input()      # Принимаем строку
text = text[::-1]   # Через срез переварачиваем строку
print(text)  





#---------- Easy C ----------#

text = input()      # Принимаем строку
l = int(input())
r = int(input())

ans = text[l:r+1]   # Срезаем список от l по r
print(ans)




#---------- Easy D ----------# 

text = input()              # Принимаем строку
middle = len(text) // 2     # Вычисляем центральный список

first_part = text[ :middle]   # Срезаем первую половину строки  (от начала до центра)
second_part = text[middle: ]  # Срезаем второую половину строки (от центра до конца)

# Первая половина маленькими буквами(метод lower), а вторая половина большими буквами(метод upper)
print(first_part.lower() + second_part.upper())






#---------- Medium A ----------#

word = input()     # Принимаем строку
ans = ""

for letter in word:      # Итерируем строку

    # Если буква маленькая 
    if letter.islower():
        ans += letter.upper()  # То добавляем его в строку ans уже как большую  
    else:
        ans += letter.lower()  # Иначе буква большая, добавляем букву как маленькую 

print(ans)





#---------- Medium B ----------#


word = input()     # Принимаем строку
# два каунтера для больших и маленьких букв
cnt_lower = 0
cnt_upper = 0

for letter in word:      # Итерируем строку

    # Если буква маленькая 
    if letter.islower():
        cnt_lower += 1   # То в количество маленьких +1
    else:
        cnt_upper += 1   # Иначе наоборот

# Чтобы узнать код нужно умножить два значения 
print("Код от замка:", cnt_lower * cnt_upper)





#---------- Medium C ----------#

word = input()     # Принимаем строку

# Слово палиндром это слово которая с любой стороны одинаково читается 
# Если слово такая же если его перевернуть, то он палиндром
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")




#---------- Hard A ----------#

text = input()     # Принимаем строку
summa = 0

for symbol in text:

    if symbol.isdigit():        # Если символ это цифра
        summa += int(symbol)    # Добавляем в сумму конвертировав в int

print("Сумма цифр среди символов:", summa)





#---------- Hard B ----------# 

text = input().lower()     # Принимаем строку, сразу же все буквы меняем на маленькие

# Самая близкая к концу алфавита самая большая по ASCII
max_symbol = max(text)     

print(max_symbol)




#---------- Hard C ----------#

text = input()       # Принимаем строку
key = int(input())   # Ключ для сдвига

ans = ""

for letter in text:  # Итерируем строку
    new_letter = letter
    # цикл на key раз чтобы букву на key раз сдвинуть
    for i in range(key):
        # Букву z дальше не сдвинешь, так что для таких случаев возвращаемся к началу алфавита 
        if new_letter == "z": 
            new_letter = "a"
        elif new_letter == "Z":
            new_letter = "A" 
        # Иначе букву сдивигаем перейдя на следующий символ по ASCII 
        else:  
            new_letter = chr(ord(new_letter) + 1)   

    # Как закончиться внутренний цикл, новую/сдвинутую букву в строку ans
    ans += new_letter


print(ans)