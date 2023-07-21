#---------- Easy A ----------#

from cw18_module import var
print(var[0])





#---------- Easy B ----------#

from cw18_module import student

print(student['name'])
print(student['age'])





#---------- Easy C ----------#

from random import randint

a = int(input("Начало: "))
b = int(input("Конец: "))

print(randint(a, b))





#---------- Medium A ----------#

from cw18_module import str_reverse

text = input("строка: ")
print("str reversed:", str_reverse(text))





#---------- Medium B ----------#

from math import sqrt, sin

x = int(input("x="))
y = int(input("y="))

res = (sqrt(sin(x) + y**3) + sqrt(x + y)) / (2*x + y)
print(res)





#---------- Medium C ----------#

from math import sin, cos, e

res = (sin(5) + 1.75**2) / (3 * e**(cos(7)))

print(res)





#---------- Hard A ----------#

from cw18_module import sum_of_max_min

numbers = list(map(int, input().split()))
print(sum_of_max_min(numbers))





#---------- Hard B ----------#

from cw18_module import count_of_letters

text = input("строка: ")
res = count_of_letters(text)

for k, v in res.items():
    print(f"{k}: {v}")
