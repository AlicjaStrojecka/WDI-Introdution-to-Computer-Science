#Zadanie 25.
#Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi
#pomimo pozbawiania ich skrajnych cyfr. Na przykład: 71317 → 131 → 3.
#Proszę napisać program, który wypisuje wszystkie takie liczby mniejsze od N.

def is_prime(number:int)->bool:
    i = 2
    while i <= number ** 0.5:
        if number % i == 0:
            return False
        i += 1
    return True

def ten_pow(number:int)->int:
    index = 0
    while number > 0:
        index += 1
        number //= 10
    return (index-1)

def is_palin(number:int)->bool:
    while number > 9:
        index = ten_pow(number)
        print(sprawdzam)
        if number % 10 == number // (10 ** index):
            number %= (10 ** index)
            number //= 10
        else:
            number = -1

def check(N:int)->int:
    for i in range(1, N+1):
        number = i
        index = ten_pow(number)
        if index % 2 == 0 and index > 1:
            if is_palin(number):
                while number > 9:
                    number %= (10 ** index)
                    number //= 10
                    if is_prime(number):
                        continue
        elif index == 0:
            print(i)
        else:
            continue


