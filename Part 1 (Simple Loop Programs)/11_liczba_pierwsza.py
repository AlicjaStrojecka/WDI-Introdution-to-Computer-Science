#Zadanie 11.
#Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

def first(num:int)->bool:
    i = 2
    while i <= num ** 0.5:
        if num % i == 0:
            return False
        i += 1
    return True

def check(num:int):
    if first(num):
        print(f"{num} jest liczbą pierwszą")
    else:
        print(f"{num} nie jest liczbą pierwsza")

check(4)