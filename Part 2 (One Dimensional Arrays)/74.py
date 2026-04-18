# Zadanie 74.
# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami
# naturalnymi wyznacza długość najdłuższego, spójnego podciągu geometrycznego.

table = [1,2,4,8,2,4]

def sequence(table:list)->int:
    max_length = 0
    print(table)
    high = len(table)
    for cycle in range(high-1):
        length = 1
        q = table[cycle + 1] / table[cycle]
        for index in range(cycle, high - 1):
            if table[index] * q != table[index + 1]:
                if max_length < length:
                    max_length = length
                break
            length += 1
            if max_length < length:
                max_length = length
    return max_length

print(sequence(table))