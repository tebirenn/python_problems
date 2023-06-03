

#---------- Easy A ----------#

numbers = set(map(int, input().split()))
res = set()

for el in numbers:
    if el % 3 != 0:
        res.add(el)

print(res)




#---------- Easy B ----------#

numbers = set(map(int, input().split()))
res = set()

for el in numbers:
    k = 0
    while el >= 2**k:
        if el == 2**k:
            res.add(el)

        k += 1

print(res)





#---------- Medium A ----------#

numbers = set(map(int, input().split()))

print(f"Максимальный элемент - {max(numbers)}")
print(f"Минимальный элемент - {min(numbers)}")




#---------- Medium B ----------#

numbers = set(map(int, input().split()))
print(len(numbers))






#---------- Hard A ----------#

numbers = list(map(int, input().split()))
res = set()

for el in numbers:
    if el in res:
        print("YES")
    else:
        print("NO")
        res.add(el)





#---------- Hard B ----------#

words = set()

n = int(input("n: "))

for i in range(n):
    sentence = input().split()
    # words.update(sentence)  # Альтернатива циклу ниже
    for word in sentence:
        word = word.replace(".", "").replace(";", "").replace(":", "").replace(",", "")
        words.add(word.lower())

print(len(words))


# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.