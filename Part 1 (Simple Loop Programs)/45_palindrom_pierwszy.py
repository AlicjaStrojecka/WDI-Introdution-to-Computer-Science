# Zadanie 45.
# Liczbę pierwszą będącą palindromem nazywamy “palindromem pierwszym”.
# Liczbę nazywamy “super palindromem pierwszym” jeżeli podczas odrzucania parami skrajnych cyfr do końca
# pozostaje ona palindromem pierwszym. Na przykład, liczba 373929373 jest super palindromem
# pierwszym bo 373929373, 7392937, 39293, 929, 2 są palindromami pierwszymi.
# Początkowymi super palindromami pierwszymi są: 2, 3, 5, 7, 11, 131, 151.
# Proszę napisać program, który wylicza ile jest super palindromów pierwszych mniejszych od zadanej liczby n.

def is_prime(number:int)->bool:
    a = 1
    sqrt = number**(0.5)
    while a <= sqrt:
        a += 1
        if number % a == 0:
            return False
    return True


def is_super_palin(palindrome:str)->bool:
    palin = str(palindrome)
    length = len(palin)
    if all(palin[i] == palin[-i - 1] for i in range(length // 2)):
        if all(is_prime(palindrome % (10**(length - j)) // 10**(j)) for j in range(0, (length//3)+1)):
            return True
    return False

def main(N:int)->int:
    all = 0
    for number in range(2, N+1):
        if is_super_palin(number):
            all += 1
    return all

print(main(151))

