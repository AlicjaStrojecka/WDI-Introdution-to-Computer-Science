# Zadanie 42.
# Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N!. Program powinien
# działać dla N rzędu 10^100.
from math import factorial

def check()->int:
    x = int(input("podaj liczbe: "))
    silnia, d = divmod(factorial(x), 10)
    while d == 0:
        silnia, d = divmod(silnia, 10)
    return d

print(check())