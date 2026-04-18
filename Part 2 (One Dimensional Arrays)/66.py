# Zadanie 66.
# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

def check(N:int)->None:
    tab = [1]*(N-1)
    for index in range(2, N + 1):
            tab[index - 2] = index
    number = 2
    sqrt = N**(0.5)
    count = 0
    while number < sqrt:
        for index in range(0, N-1):
            if tab[index] % number == 0 and tab[index] != number:
                tab[index] = 0
        number += 1
    for index in range(0, N-1):
        if tab[index] != 0:
            count += 1
            print(tab[index], end = " ")
check(100)