# Zadanie 76.
# Proszę napisać program, który wypełnia N-elementową tablicę T trzycyfrowymi liczbami
# pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
# znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
# Na przykład dla tablicy: t= [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4

from random import randint

def sequence()->int:
    N = int(input(""))
    table = [randint(100,999) for _ in range(N)]
    length = len(table)
    highest = 0
    for position in range(length):
        current = ""
        for right in range(position, length):
            current += str(table[right])
            reverse = current[::-1]
            for shift in range(0, length-len(current)+1):
                if shift + len(current) <= position or shift >= len(current) + position :
                    fragment = ''.join(str(table[x]) for x in range(shift, shift + len(current)))
                    if reverse == fragment:
                        if highest < len(current):
                            highest = len(current)

    return highest

print(sequence())



