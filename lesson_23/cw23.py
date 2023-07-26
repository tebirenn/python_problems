from math import sqrt

#---------- Easy C ----------#

class Country:                                  # Создали класс Country

    def __init__(self, p: int) -> None:         # Инизиализация чтобы создать популизацию
        self.__population = p                   # Популяция являеться приватным

    def get_population(self) -> int:            # По этой причине создан геттер для неё
        return self.__population
    
    def set_population(self, new_p) -> None:    # И сеттер
        self.__population = new_p


class Russia(Country):                          # Три класса стран, наследующих от класса Country
    pass

class Canada(Country):
    pass

class Germany(Country):
    pass


r = Russia(143_400_000)                         # Создаем объектов трех дочерних классов
c = Canada(38_250_000)
g = Germany(83_000_000)

g.set_population(83_200_000)                    # Показываем работоспособность геттеров и сеттеров

print(r.get_population())
print(c.get_population())
print(g.get_population())





#---------- Easy A ----------#

class Games:                                    # Создаем класс Games
    def __init__(self, y: int, game_name: str) -> None:
        self.year = y                           # Инициализация создает два атрибута год выхода и название игры
        self.name = game_name

    def get_name(self) -> str:                  # Геттер для названия игры
        return self.name
    

class PCGames(Games):                           # Комп. игры дополнительно нужнаються в минимальных требованиях
    def __init__(self, y: int, game_name: str, min_reqs: dict) -> None:
        super().__init__(y, game_name)
        self.minimal_requirements = min_reqs

class PSGames(Games):                           # PS игры требуют версию игровой консоли(числовой)
    def __init__(self, y: int, game_name: str, ps_version: int) -> None:
        super().__init__(y, game_name)
        self.ps_version = ps_version

class XboxGames(Games):                         # Xbox игры так же требуют версию(строковой)
    def __init__(self, y: int, game_name: str, xbox_version: str) -> None:
        super().__init__(y, game_name)
        self.xbox_version = xbox_version

class MobileGames(Games):                       # Мобильные игры требуют тип ОС
    def __init__(self, y: int, game_name: str, os_type: str) -> None:
        super().__init__(y, game_name) 
        self.os_type = os_type


# Создали объект каждого дочернего класса
cs = PCGames(2012, "CS:GO", {"processor": "Intel i5, 10th gen", "videocard": "Nvidia GTX 1050"})
tlos2 = PSGames(2020, "The Last Of US II", 5)
sot = XboxGames(2018, "Sea of Thieves", "Series S|X")
ss = MobileGames(2012, "Subway Surfers", "iOS")





#---------- Medium A ----------#

class Human:                        # класс Human
    def __init__(self, name: str, age: int, country: str) -> None:
        self.name = name            # с атрибутами имени, возраста и страны 
        self.age = age
        self.country = country

class Student(Human):               # класс Student наследник класса Human
    def __init__(self, name: str, age: int, country: str, university_name: str, gpa: float) -> None:
        super().__init__(name, age, country)        # Три атрибута будут созданы родителем 
        self.university_name = university_name      # А два дополнительных атрибута будут созданы тут
        self.gpa = gpa

                                                    # Создаем объект класса Student
std1 = Student("Abay", 18, "Kazakhstan", "KBTU", 3.56)

print("Name:", std1.name)                           # Выводим все данные
print("Age:", std1.age)
print("Country:", std1.country)
print("University:", std1.university_name)
print("GPA:", std1.gpa)





#---------- Medium B ----------#

class Shape:                                        # Родительский класс Shape
    def get_area(self) -> int:                      # с методом get_area() возвращающии 0, потому что это не конкретная фигура
        return 0
    
class Triangle(Shape):                              # класс Triangle наследнует от класса Shape
    def __init__(self, a, b, c) -> None:            # Инициализация создает три стороны треугольника
        self.a = a
        self.b = b 
        self.c = c

    def get_area(self) -> float:                    # Переписываем метод get_area() для треугольника
        p_half = (self.a + self.b + self.c) / 2     # Для того чтобы вычислить площадь, нужно знать сколько будет половина периметра
                                                    # Вычисляем теперь площадь по формуле трех сторон
        return sqrt(p_half * (p_half - self.a) * (p_half - self.b) * (p_half - self.c))
    

class Square(Shape):                                # класс Square наследнует от класса Shape                
    def __init__(self, a) -> None:                  # Инизиализация принимает одно значение, сторона квадрата
        self.a = a

    def get_area(self) -> int|float:                # Для этого класса тоже переписываем родительский get_area()
        return self.a**2                            # Площадь равна к квадрату одной стороны
    

num = int(input())                  # Принимаем одно число с консоли
shape_obj = Shape()                 # Создаем объект неизвестной фигуры
square_obj = Square(num)            # Создаем объект квадрата передав значение принятое с консли

print(shape_obj.get_area())         # Для обеих классов вызываем метод get_area()
print(square_obj.get_area())





#---------- Hard A ----------#

class Shop:                                                                 # Создали класс Shop
    def __init__(self, products_list: dict) -> None:                        # При инициализаций принимаем словарь продуктов где ключи это название продукта, а значения это цена продукта
        self.__products = products_list                                     # Сохранили продукты в атрибут products(приватный)
        self.__basket = dict.fromkeys(self.__products.keys(), 0)            # Создаем словарь корзины(приватный). Ключи: названия продукта, Значения: количество продукта(изначально у всех продуктов будет 0)


    def add_product(self, prdct_name: str, prdct_cnt: int) -> None:         # Метод чтобы добавить продукт в корзину, принимаем название продукта и количество

        if prdct_name not in self.__products:                               # Сначала проверяем, вдруг этого продукта нет в магазине
            print(f"Продукт {prdct_name} у нас нет!\n")                     # Если так и есть, то сообщаем об этом 
        else:                                                               # Иначе продукт у нас есть
            self.__basket[prdct_name] += prdct_cnt                          # Добавляем указанное количество к товару в корзине и информируем об этом 
            print(f"Продукс {prdct_name} успешно добавлен в корзину, количество: {self.__basket[prdct_name]}\n")

    
    def remove_product(self, prdct_name: str, prdct_cnt: int) -> None:      # Метод чтобы убрать продукт из корзины, принимаем название продукта и количество

        if prdct_name not in self.__products:                               # Сначала проверяем, вдруг этого продукта нет в магазине
            print(f"Продукт {prdct_name} у нас нет!\n")                     # Если так и есть, то сообщаем об этом 
        else:                                                               # Иначе продукт у нас есть
            self.__basket[prdct_name] -= prdct_cnt                          # Минусуем указанное количество товара из корзины
            if self.__basket[prdct_name] < 0:                               # Если количество ушел в минус
                self.__basket[prdct_name] = 0                               # Просто сами установим вместо этого 0
                                                                            # И информируем пользователя
            print(f"Продукс {prdct_name} успешно убран из корзины, количество: {self.__basket[prdct_name]}\n")

    
    def product_list(self) -> None:                                         # Метод чтобы показать что есть у пользователя в корзине

        print("Список продуктов из корзины:")
        for prdct_name, prdct_cnt in self.__basket.items():                 # Пробегаемся по корзине
            if prdct_cnt > 0:                                               # Нужно показать только те продукты у которых количество 1 или более
                print(f"Имя продукта: {prdct_name}, количество: {prdct_cnt}, общяя цена: {prdct_cnt * self.__products[prdct_name]}$")
                                                                            # Чтобы показать общую цену, нужно умножить количество товара к цене(Цена храниться в словаре products)
        print() # Для отступа

    
    def __all_cost(self) -> int:                                            # Приватный метод чтобы узнать общую цену всех продуктов
        res = 0                                                             # Переменная куда будет все суммироваться

        for prdct_name, prdct_cnt in self.__basket.items():                 # Пробегаемся по корзине
            res += prdct_cnt * self.__products[prdct_name]                  # Вычисляем общую сумму одного продукта по той же схеме: количество*цена

        return res                                                          # Как цикл закончит свою работу, возвращаем сумму
    
    def __avg_cost(self) -> float:                                          # Приватный метод чтобы узнать среднюю цену одного продукта
                                                                            # Для этого нужно сумму поделить на количество
        all_cnt = sum(self.__basket.values())                               # Вычисляем всё количество из корзины, сумма всех значений из словаря basket(количество продуктов в значений этого словаря)       
        return self.all_cost() / all_cnt                                    # Сумму получим через метод all_cost, делим его на количество которую только что вычислили
    
