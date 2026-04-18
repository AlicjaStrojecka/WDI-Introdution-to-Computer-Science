#Zadanie 12.
#Proszę napisać program wypisujący podzielniki liczby.

def div(num: int):
    for i in range(2, num+1):
        if num % i == 0:
            print(i)
    return False

div(32)