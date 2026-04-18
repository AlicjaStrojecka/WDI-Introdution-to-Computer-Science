# Zadanie 39.
# Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
# zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać
# te elementy ciągu które są równe średniej arytmetycznej z 4 najbliższych sąsiadów.
# Na przykład dla ciągu: 2,3,2,7,1,2,4,8,5,2,2,5,7,9,3,1,0 powinny zostać wypisane
# liczby: 4,5. Można założyć, że w ciągu znajduje się co najmniej 5 elementów.

def check()->None:
    i1, i2, i3, i4, i5 = (int(input()) for i in range(1, 6)))

    while i5 != 0:
        if (i1 + i2 + i3 + i4) // 4 == i5:
            print(i5)

        i1, i2, i3, i4, i5 = i2, i3, i4, i5, int(input())