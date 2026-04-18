#Zadanie 15.
#Dwie różne liczby nazywamy zaprzyjaźnionymi, gdy każda jest równa sumie
#podzielników właściwych drugiej liczby, na przykład 220 i 284. Proszę
#napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def factors(number:int)->int:
    const_number = number
    factor = 2
    sum = 1
    while factor ** 2 < number:
        if number % factor == 0:
            sum += factor + const_number//factor
        factor += 1
    return sum

def check():
    for i in range(220, 1000000):
        for j in range(i+1, 1000000):
            if factors(i) == j and factors(j) == i:
                print(factors(i), factors(j))

check()