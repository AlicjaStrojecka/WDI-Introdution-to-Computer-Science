# Zadanie 40.
# Napisać program, który wyznacza liczbę zer jakimi kończy się liczba N!
# Program powinien działać dla N rzędu 10^100
from math import factorial

def check()->int:
    x = int(input("podaj liczbe: "))
    zeros = 0
    silnia, d = divmod(factorial(x), 10)

    while d == 0:
        zeros += 1
        silnia, d = divmod(silnia, 10)

    return zeros

print(check())