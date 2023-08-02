#---------- Easy ----------#

class University:                               # Создаем родительский класс University
    def __init__(self, off_name: str, location: str) -> None:
        self.off_name = off_name                # При инициализаций принимаем 2 значения: off_name, location
        self.location = location                # И сохраняем их в атрибуты off_name, location


class Professor(University):                    # Создаем класс Proferssor наследника класса University
                                                # Принимает 2 значения как у родителя и full_name, subject
    def __init__(self, off_name: str, location: str, full_name: str, subject: str) -> None:
        super().__init__(off_name, location)    # off_name, location отправляем в родительский конструктор
        self.full_name = full_name              # А два остальных значения сохраним здесь
        self.subject = subject


class Student(University):                      # Создаем класс Student наследника класса University
                                                # Принимает 2 значения как у родителя и full_name, speciality
    def __init__(self, off_name: str, location: str, full_name: str, speciality: str) -> None:
        super().__init__(off_name, location)    # off_name, location отправляем в родительский конструктор
        self.full_name = full_name              # А два остальных значения сохраним здесь
        self.speciality = speciality





#---------- Medium ----------#

class Table:                                    # Создаем класс Table
    def __init__(self, l, w, h) -> None:        # Инициализация принимает 3 числа 
        self.length = l                         # Сохраняем из как длину, ширину и высоту
        self.width = w
        self.height = h


class DeskTable(Table):                         # Создаем класс DeskTable наследника класса Table
                                                # Инициализацию создавать не будем, потому что будем пользоваться родительским
    
    def get_area(self) -> int|float:            # Создадим метод для вычисления площади поверхности   
        return self.length * self.width         # Метод возвращает умножение длины к ширине


a, b, c = map(float, input().split())           # Принимаем три числа с консоли
dt = DeskTable(a, b, c)                         # Через них создаем объект класса DeskTable

print(dt.get_area())                            # Через созданный объект вызываем метод get_area()





#---------- Hard ----------#

class ComputerTable(DeskTable):                 # Создаем класс ComputerTable наследника класса DeskTable
    def __init__(self, l, w, h, ma) -> None:    # Сюда придеться писать свою инициализацию, так как у нас есть дополнительное значение
        super().__init__(l, w, h)               # 3 значения отправляем родителям
        self.monitor_area = ma                  # Одну лишнюю сохраняем сами

    def get_free_area(self) -> int|float:       # Создаем метод чтобы вычислить свободное место, чтобы это сделать нужно от общей площади отнимаем площадь монитора
        return super().get_area() - self.monitor_area       # Общюю площадь узнаем через родительский метод get_area() и минусуем от него площадь монитора
    

a, b, c, d = map(float, input().split())        # Принимаем 4 числа с консоли
ct = ComputerTable(a, b, c, d)                  # Создаем через них объект класса ComputerTable

print(ct.get_free_area())                       # И вызываем метод get_free_area() и выводим ответ метода 