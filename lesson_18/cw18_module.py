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
    return string[::-1]

#---------- Hard A ----------#

def sum_of_max_min(nums: list) -> int|float:
    max_el = max(nums)
    min_el = min(nums)

    return max_el + min_el

#---------- Hard B ----------#

def count_of_letters(string: str) -> dict:
    res = dict.fromkeys(string)

    for letter in string:
        res[letter] += 1

    return res