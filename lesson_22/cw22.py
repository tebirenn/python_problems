from math import sqrt

#---------- Easy A ----------#

class Point:        # Создали класс
    x = 5           # Создали два атрибута x и y
    y = 10

p = Point()         # Создаем объект созданного класса 

letter = input()    # Принимаем одну букву
if letter == "x":   # Если эта буква "x"
    print(p.x)      # Выводим атрибут "x" из объекта 
elif letter == "y": # Иначе-если это "y"
    print(p.y)      # Выводим атрибут "y" из объекта





#---------- Easy B ----------#

class Point:        # Создаем класс
    def __init__(self, num1, num2) -> None:     # Добавляем инициализацию с двумя значениями
        self.x = num1                           # Из двух значений создаем атрибуты x и y
        self.y = num2

n1 = int(input())   # Принимаем два числа с консоли
n2 = int(input())
p = Point(n1, n2)   # Создаем объект созданного класса передав два значения принятые с консоли

letter = input()    # Принимаем одну букву
if letter == "x":   # Если эта буква "x"
    print(p.x)      # Выводим атрибут "x" из объекта 
elif letter == "y": # Иначе-если это "y"
    print(p.y)      # Выводим атрибут "y" из объекта





#---------- Easy C ----------#

class Point:        # Создаем класс
    def __init__(self, num1, num2) -> None:     # Добавляем инициализацию с двумя значениями
        self.x = num1                           # Из двух значений создаем атрибуты x и y
        self.y = num2

    def dist(self, other_point) -> float:       # Создаем метод dist для вычисления дистанций между двумя точками, принимает один аргумент(другая точка )
        return sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)      # Чтобы узнать дистанцию, используем формулу показанную в задаче

n1 = int(input())   # Принимаем два числа с консоли
n2 = int(input())
p1 = Point(n1, n2)  # Создаем первый объект созданного класса передав два значения принятые с консоли

n3 = int(input())   # Принимаем ещё два числа с консоли
n4 = int(input())
p2 = Point(n3, n4)  # Создаем второй объект созданного класса передав два значения принятые с консоли

print("Дистанция двух точек:", p1.dist(p2))     # Выводим ответ задачи, вызвав метод dist из первой точки, и передав в качестве other_point вторую точку





#---------- Medium A ----------#

class Rect:     # Создаем класс Rect
    def __init__(self, l: int|float, w: int|float):     # Добавляем инициализацию с двумя значениями
        self.length = l                     # Первое значение сохраняем как длину
        self.width = w                      # Вторую как ширину

    def is_square(self) -> bool:            # Создаем метод is_square. Возвращает bool значение
        return self.length == self.width    # Возвращаем ответ сравнения равны ли длина и ширина(Ответ будет True или False)
    

a = int(input())        # Принимаем два числа с консоли  
b = int(input())
r1 = Rect(a, b)         # Создаем объект класса Rect и передаем те два значения с консоли для инициализаций 

print(r1.is_square())   # Вызываем метод is_square и выводим ответ функций 





#---------- Medium B ----------#

class Rect:     # Создаем класс Rect
    def __init__(self, l: int|float, w: int|float):     # Добавляем инициализацию с двумя значениями
        self.length = l                     # Первое значение сохраняем как длину
        self.width = w                      # Вторую как ширину

    def is_square(self) -> bool:            # Создаем метод is_square. Возвращает bool значение
        return self.length == self.width    # Возвращаем ответ сравнения равны ли длина и ширина(Ответ будет True или False)
    
    def get_perimeter(self) -> int|float:       # Метод чтобы узнать периметр
        return (self.length + self.width) * 2   # Удвоенная сумма двух сторон прямоугольника
    
    def get_area(self) -> int|float:            # Метод чтобы узнать площадь
        return self.length * self.width         # Произведение двух сторон прямоугольника
    
    def get_diagonal(self) -> float:                # Метод чтобы узнать диагональ 
        return sqrt(self.length**2 + self.width**2) # По формуле гиппотенузы
    

a = int(input())        # Принимаем два числа с консоли  
b = int(input())
r1 = Rect(a, b)         # Создаем объект класса Rect и передаем те два значения с консоли для инициализаций 

print(r1.get_perimeter())       # Вызываем новые созданные три метода и показываем из работоспособность
print(r1.get_area())
print(r1.get_diagonal())





#---------- Hard A ----------#

class Shop:                                                                 # Создали класс Shop
    def __init__(self, products_list: dict) -> None:                        # При инициализаций принимаем словарь продуктов где ключи это название продукта, а значения это цена продукта
        self.products = products_list                                       # Сохранили продукты в атрибут products
        self.basket = dict.fromkeys(self.products.keys(), 0)                # Создаем словарь корзины. Ключи: названия продукта, Значения: количество продукта(изначально у всех продуктов будет 0)


    def add_product(self, prdct_name: str, prdct_cnt: int) -> None:         # Метод чтобы добавить продукт в корзину, принимаем название продукта и количество

        if prdct_name not in self.products:                                 # Сначала проверяем, вдруг этого продукта нет в магазине
            print(f"Продукт {prdct_name} у нас нет!\n")                     # Если так и есть, то сообщаем об этом 
        else:                                                               # Иначе продукт у нас есть
            self.basket[prdct_name] += prdct_cnt                            # Добавляем указанное количество к товару в корзине и информируем об этом 
            print(f"Продукс {prdct_name} успешно добавлен в корзину, количество: {self.basket[prdct_name]}\n")

    
    def remove_product(self, prdct_name: str, prdct_cnt: int) -> None:      # Метод чтобы убрать продукт из корзины, принимаем название продукта и количество

        if prdct_name not in self.products:                                 # Сначала проверяем, вдруг этого продукта нет в магазине
            print(f"Продукт {prdct_name} у нас нет!\n")                     # Если так и есть, то сообщаем об этом 
        else:                                                               # Иначе продукт у нас есть
            self.basket[prdct_name] -= prdct_cnt                            # Минусуем указанное количество товара из корзины
            if self.basket[prdct_name] < 0:                                 # Если количество ушел в минус
                self.basket[prdct_name] = 0                                 # Просто сами установим вместо этого 0
                                                                            # И информируем пользователя
            print(f"Продукс {prdct_name} успешно убран из корзины, количество: {self.basket[prdct_name]}\n")

    
    def product_list(self) -> None:                                         # Метод чтобы показать что есть у пользователя в корзине

        print("Список продуктов из корзины:")
        for prdct_name, prdct_cnt in self.basket.items():                   # Пробегаемся по корзине
            if prdct_cnt > 0:                                               # Нужно показать только те продукты у которых количество 1 или более
                print(f"Имя продукта: {prdct_name}, количество: {prdct_cnt}, общяя цена: {prdct_cnt * self.products[prdct_name]}$")
                                                                            # Чтобы показать общую цену, нужно умножить количество товара к цене(Цена храниться в словаре products)
        print() # Для отступа

    
    def all_cost(self) -> int:                                              # Метод чтобы узнать общую цену всех продуктов
        res = 0                                                             # Переменная куда будет все суммироваться

        for prdct_name, prdct_cnt in self.basket.items():                   # Пробегаемся по корзине
            res += prdct_cnt * self.products[prdct_name]                    # Вычисляем общую сумму одного продукта по той же схеме: количество*цена

        return res                                                          # Как цикл закончит свою работу, возвращаем сумму
    
    def avg_cost(self) -> float:                                            # Метод чтобы узнать среднюю цену одного продукта
                                                                            # Для этого нужно сумму поделить на количество
        all_cnt = sum(self.basket.values())                                 # Вычисляем всё количество из корзины, сумма всех значений из словаря basket(количество продуктов в значений этого словаря)       
        return self.all_cost() / all_cnt                                    # Сумму получим через метод all_cost, делим его на количество которую только что вычислили
    

p = {               # Создаем словарь продуктов
    "milk": 10,
    "water": 5,
    "bread": 15,
    "tomato": 8,
    "apple": 6
}
my_shop = Shop(p)   # Создаем объект класса Shop, передав словарь из продуктов для данного магазина

# Вызываем методы(с разными кейсами) показывая из работоспособность
my_shop.add_product("milk", 5)
my_shop.add_product("milk", 2)
my_shop.add_product("bread", 2)
my_shop.add_product("sigarettes", 2)
my_shop.add_product("water", 5)

my_shop.remove_product("vodka", 1)
my_shop.remove_product("milk", 3)

my_shop.product_list()

print(f"Общяя цена продуктов: {my_shop.all_cost()}$")
print(f"Средняя цена одного продукта в магазине: {my_shop.avg_cost():.2f}$")
