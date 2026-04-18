# Zadanie 72.
# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami
# naturalnym wyznacza długość najdłuższego, spójnego podciągu rosnącego.

from random import randint

table = [randint(0,10) for i in range(10)]

def sequence(table:list)->int:
    max_length = 0
    print(table)
    high = len(table)
    for cycle in range(high):
        length = 1
        for index in range(cycle, high - 1):
            if table[index] >= table[index + 1]:
                if max_length < length:
                    max_length = length
                break
            length += 1
    return max_length

print(sequence(table))
