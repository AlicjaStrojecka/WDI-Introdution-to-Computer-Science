#Zadanie 30.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
#ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

def check(number:int)->bool:
    i = 1
    a = 3
    while a <= number:
        if number % a == 0:
            return True
        i += 1
        a = i * i + i + 1
    return False

for i in range(10):
    print(i, check(i))