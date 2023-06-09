

#---------- Easy A ----------#

keys = ["Ten", "Twenty", "Thirty"] 
values = [10, 20, 30] 

res = dict(zip(keys, values))
print(res)





#---------- Easy B ----------#

sample_dict = { 
    "class": { 
        "student": { 
            "name": "Mike", 
            "marks": { 
                "physics": 70, 
                "history": 80 
            } 
        } 
    } 
} 

print(sample_dict["class"]["student"]["marks"]["history"])





#---------- Easy C ----------#

d = { 
    "math": 75, 
    "physics": 90, 
    "ict": 64, 
    "ads": 70 
}

min_value = min(d.values())

for k, v in d.items():
    if v == min_value:
        print(k)




#---------- Easy D ----------#

info = {
    "name": "Aidana",
    "grades": [96, 78, 67, 73, 90]
}

aidana_grades = info["grades"]

res = sum(aidana_grades) / len(aidana_grades)
print(res)





#---------- Medium A ----------#

journal = {}
n = int(input("n: "))

for i in range(n):
    name, grade = input().split()
    journal[name] = int(grade)

print("name | grade")
for k, v in journal.items():
    print(f"{k}: {v}")





#---------- Medium B ----------#

words = input().split()
words_count = dict.fromkeys(words, 0)

for word in words:
    words_count[word] += 1

for word, count in words_count.items():
    print(word, count)





#---------- Medium C ----------#

### в задаче надо было сказать какие числа сколько раз встречались 

number = abs(int(input("число: ")))
num_cnt = {}

while number != 0:
    last_digit = number % 10

    if last_digit not in num_cnt.keys():
        num_cnt[last_digit] = 0

    num_cnt[last_digit] += 1

    number //= 10

for k, v in num_cnt.items():
    print(k, v)




#---------- Hard A ----------#

journal = {}
n = int(input("n: "))
all_grades = 0

for i in range(n):
    name, grade = input().split()
    all_grades += int(grade)

    if name not in journal.keys():
        journal[name] = 0
    
    journal[name] += int(grade)

for k, v in journal.items():
    print(f"{k}: {(v*100) / all_grades}%")





#---------- Hard B ----------#

accounts = {}

n = int(input("n: "))
for i in range(n):
    login, password = input().split()
    accounts[login] = password

n = int(input("n: "))
for i in range(n):
    login, password = input().split()

    if login not in accounts.keys():
        print("user not defined")
    elif accounts[login] == password:
        print("welcome")
    else:
        print("wrong password")
    




#---------- Hard C ----------#

word = input()
letter_cnt = dict.fromkeys(word, 0)

for letter in word:
    letter_cnt[letter] += 1

odd_count = 0
for value in letter_cnt.values():
    if value % 2 == 1:
        odd_count += 1

if odd_count > 1:
    print("wasted")
else:
    print("we can do it")