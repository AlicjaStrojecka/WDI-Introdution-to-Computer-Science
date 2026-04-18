#Zadanie 32.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający
#na pytanie, czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu
#danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2.

def check(x:int)->bool:
    A = 2
    while A <= x:
        if x % A == 0:
            return True
        A = 3 * A + 1
    return False

print(check(13))