# Zadanie 75.
# Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością
# najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością
# najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami
# ciągu są elementy tablicy o kolejnych indeksach.

from random import randint

def sequence(N:int)->int:
    table = [randint(1,99) for i in range(N)]
    print(table)
    max_pos, max_neg = 1, 1
    for cycle in range(N-1):
        length = 1
        r = table[cycle + 1] - table[cycle]
        for index in range(cycle, N-1):
            if table[index] + r != table[index + 1]:
                if r > 0 and length > max_pos:
                    max_pos = length
                if r <= 0 and length > max_neg:
                    max_neg = length
                break
            length += 1
            if r > 0 and length > max_pos:
                max_pos = length
            if r < 0 and length > max_neg:
                max_neg = length

    return max_pos - max_neg

print(sequence(7))