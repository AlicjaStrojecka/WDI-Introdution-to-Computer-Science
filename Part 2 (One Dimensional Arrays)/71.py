# Zadanie 71.
# Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k].
# Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
from random import randint
from math import isqrt

def is_prime(number:int)->bool:
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
    for i in range(5, isqrt(number) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def get_factors(number:int):
    return [factor for factor in range(2, number + 1) if is_prime(factor) and number % factor == 0]

def check(N:int)->bool:
    table = [randint(0,1000) for i in range(N)]
    print(table)
    can_jump = [False] * len(table)
    can_jump[0] = True
    a = 0
    while a < N:
        if can_jump[a] == True:
            for factor in get_factors(a):
                if factor + a < N:
                    can_jump[factor + a] == True
                    if can_jump[-1] == True:
                        return can_jump[-1]
        a += 1
    return can_jump[-1]
print(check(10))