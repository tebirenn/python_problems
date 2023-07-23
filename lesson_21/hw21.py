import os
import shutil

#---------- Easy ----------#

def is_exist_file(file_name: str) -> bool:
    try:                                    # Для того чтобы узнать есть ли данный файл
        open(file_name, "r").close()        # Попытаемся его прочитать
    except FileNotFoundError:
        return False                        # Если возникнет исключение FileNotFoundError, то файла нет False
    else:
        return True                         # Если всё таки есть, то True


while True:                         # Запускаем бесконечный цикл и начинаем принимать название файла 
    file_name = input("Введите название файла: ")

    if is_exist_file(file_name):    # Отправляем введенное название в функцию чтобы узнать существует ли данный файл
        break                       # Если да, то ломаем цикл
    else:                           # Иначе просто информируем о том что файла нет, затем цикл перезапускается чтобы пользователь еще раз ввел название файла
        print(f"Файла {file_name} не существует, попробуйте еще!")

file = open(file_name, "r", encoding="utf-8")   # После того как цикл завершается, открываем файл для чтения 

for i in range(5):              # Запускаем цикл на 5 раз
    line = file.readline()      # Читаем одну линию
    print(line.strip("\n"))     # Выводим прочитанную линию(убрав \n который там уже есть)

file.close()                    # Закрываем файл





#---------- Medium ----------#

file = open("ethics.txt", "r", encoding="utf-8")

lines = file.readlines()        # Читаем все линий одним списком 

print("Нечетные линий:")        # Нечетные линий будут начинатсья с 0 индекса  
print(*lines[::2], sep="")      # Делаем срез от начала до конца, с шагом 2(чтобы попадать только на нечетные линий)

print("\nЧетные линий:")
print(*lines[1::2], sep="")     # Тоже самое для четных, просто индекс начало среза будет равна к 1


file.close()                    # Работа закончена, закрываем файл





#---------- Hard  ----------#

# --1
open("new_ethics.txt", "x").close()


# --2
ethics = open("ethics.txt", "r", encoding="utf-8")
new_ethics = open("new_ethics.txt", "w")

for i in range(6):
    line = ethics.readline()
    new_ethics.write(line)

ethics.close()
new_ethics.close()


# --3 --4 --5

for i in range(1, 4): # i = 1, 2, 3
    shutil.copy("new_ethics.txt", f"new_ethics_copy{i}.txt")
    os.mkdir(f"ethics{i}")
    shutil.move(f"new_ethics_copy{i}.txt", f"ethics{i}")


# --6
os.remove("new_ethics.txt")
