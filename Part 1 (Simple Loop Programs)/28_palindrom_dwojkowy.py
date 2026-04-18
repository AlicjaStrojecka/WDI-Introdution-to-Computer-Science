#Zadanie 28.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający
#na pytanie, czy liczba naturalna jest palindromem, a następnie czy
#jest palindromem w systemie dwójkowym.

from decimal import Decimal

def is_palin(number:int, system:int )->bool:
    power = len(str(number)) - 1
    while number > 9:
        if number // (10 ** (power)) != number % 10:
            return False
        number //= 10
        number %= 10 ** (power - 1)
        power -=2
        continue
    if power % 2 == 1 and number == 1 and system == 2:
        return False
    return True

def binary(number:int)->bool:
    binnum = int(bin(number)[2:])
    if is_palin(binnum, 2):
        return True
    return False

def check(number:int)->str:
    if is_palin(number, 10):
        print(f"{number} jest palindromem w systemie dziesiętnym,", end =' ')
        if binary(number):
            print("jak i w systemie dwójkowym")
        else:
            print("lecz nie jest w dwójkowym")
    else:
        print(f"liczba {number} nie jest palindromem")

for i in range(1, 23):
    check(i)