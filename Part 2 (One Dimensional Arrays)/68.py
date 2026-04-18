# Zadanie 68.
# Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
# zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien
# wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu. Można założyć, że w
# ciągu znajduje się wystarczająca liczba elementów.

def check()->int:
    largest = [0]*10
    while True:
        x = int(input())
        if x == 0: break
        for index in range(10):
            if x > largest[index]:
                jdex = 9
                while jdex > index:
                    largest[jdex] = largest[jdex-1]
                    jdex -= 1
                largest[index] = x
                break
        print(largest)
    return largest[9]

print(check())