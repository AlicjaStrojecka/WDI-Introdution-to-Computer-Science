# Zadanie 70.
# Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.

from random import randint

def has_odd(number:int)->bool:
    while number > 0:
        number, digit = divmod(number, 10)
        if digit % 2 == 0:
            return False
    return True

def check(N:int)->bool:
    table = [randint(1,1000) for i in range(N)]
    print(table)
    if any(has_odd(table[i]) for i in range(10)):
        return True
    return False

print(check(10))