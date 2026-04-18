#Zadanie 14.
#Liczba doskonała to liczba równa sumie swoich podzielników właściwych
#(mniejszych od jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać
#program wyszukujący liczby doskonałe mniejsze od miliona.

def primes(number:int)->int:
    const_number = number
    factor = 2
    sum = 1
    while factor ** 2 < number:
        if number % factor == 0:
            sum += factor + const_number//factor
        factor += 1
    if const_number == sum:
        return sum

def check():
    for number in range(2, 1000000+1):
        if primes(number):
            print(primes(number))

check(28)