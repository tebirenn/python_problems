import os
import shutil
import re

#---------- Easy A ----------#

open("task1.txt", "x").close()      # Создаем файл через мод "x"
print("Файл успешно был создан!")   # Информируем об этом





#---------- Easy B ----------#

os.remove("task1.txt")              # Удаляем файл через функцию remove
print("Файл успешно был удалён!")   # Файл успешно был удалён!





#---------- Easy C ----------#

name = input("Имя файла: ")
format = input("Формат файла: ")

try:                                    
    open(f"{name}.{format}", "x").close() # Пытаемся создать файл с данным названием
except FileExistsError:
    print(f"Файл \"{name}.{format}\" уже создан!") # Если файл уже создан, возникает исключение FileExistsError
else:
    print(f"Файл \"{name}.{format}\" успешно был создан!") # Если же все пошло по плану





#---------- Easy D ----------#

full_file_name = input()

try:
    os.remove(full_file_name) # Пытаемся удалить файл с данным названием 
except FileNotFoundError:
    print(f'Файл "{full_file_name}" не найден!') # Если такого файла не существует
else:
    print(f'Файл "{full_file_name}" успешно был удалён!') # Если же все пошло по плану
    




#---------- Medium A ----------#

old_name = input()
new_name = input()

try:
    os.rename(old_name, new_name)   # Пытаемся переименовать файл
except FileNotFoundError:
    print("Error")                  # Если файл не найден
else:
    print("Done")                   # Если файл был переименован





#---------- Medium B ----------#

file = open("medium.txt", "w", encoding="utf-8")    # Открываем для перезаписи

size = int(input())                 # Принимаем количество строк ввода

for i in range(size):               # Запускаем цикл на Size раз
    new_line = input()              # Принимаем строку
    file.write(new_line + "\n")     # Записываем данную строку в файл  

file.close()                                        # Закрываем файл





#---------- Medium C ----------#

file = open("medium.txt", "w", encoding="utf-8")    # Открываем для дозаписи

size = int(input())                 # Принимаем количество строк ввода

for i in range(size):               # Запускаем цикл на Size раз
    new_line = input()              # Принимаем строку
    file.write(new_line + " ")      # Записываем данную строку в файл через пробел

file.close()                                        # Закрываем файл





#---------- Hard A ----------#

file = open("hardA.txt", "r", encoding="utf-8") # Открываем файл для чтения

inner = file.read()         # считываем все содержимое файла в переменную inner
print(inner.upper())        # Выводим переменную inner применив метод upper

file.close()                                    # Закрываем файл





#---------- Hard B ----------#

read_file = open("hardB.txt", "r", encoding="utf-8")    # Открываем файл hardB.txt для чтения
write_file = open("decode.txt", "w")                    # decode.txt для записи

inner = read_file.read()    # считываем все содержимое файла hardB.txt в переменную inner
write_file.write(inner)     # Записываем все считанное в файл decode.txt

read_file.close()           # Закрываем оба файла
write_file.close()
os.remove("hardB.txt")      # В конце удаляем файл hardB.txt





#---------- Hard C ----------#

file = open("hardC.txt", "r", encoding="utf-8")     # Открываем файл hardC.txt для чтения 

inner = file.read()                                 # считываем все содержимое файла hardB.txt в переменную inner
# Все слова из содержимого файла найдем через regex findall
words = re.findall(r"[a-z]+", inner, flags=re.IGNORECASE)

for word in words:              # Пробегаемся по всем словам из списка words
    if word == word[::-1]:      # Если слово такой же если его перевернуть 
        print(word)             # То он является палиндромом

file.close()                    # Закрываем файл 
