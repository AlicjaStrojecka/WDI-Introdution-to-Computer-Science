#Zadanie 13.
#Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze

def primes(number:int)->int:
    factor = 2
    while factor ** 2 <= number:
        while number % factor == 0:
            number = number//factor
            print(factor)
        factor += 1
    if number > 1:
        print(number)

primes(28)