# Zadanie 69.
# Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000
# i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą
from random import randint

def has_odd(number:int)->bool:
    while number > 0:
        number, digit = divmod(number, 10)
        if digit % 2 == 1:
            return True
    return False

def check(N:int)->bool:
    table = [randint(1,1000) for i in range(N)]
    print(table)
    if all(has_odd(table[i]) for i in range(10)):
        return True
    return False

print(check(10))
