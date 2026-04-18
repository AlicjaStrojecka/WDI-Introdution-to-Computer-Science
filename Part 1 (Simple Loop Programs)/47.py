# Zadanie 47.
# Mając daną dodatnią liczbę całkowitą N, stwórzmy nową liczbę dodając kwadraty cyfr liczby N.
# Można udowodnić, że postępując w ten sposób wielokrotnie otrzymamy w końcu wynik 1 lub 4.
# Przykład: 13 = 12 + 32 = 1 + 9 = 10 (Krok 1) 10 = 12 + 02 = 1 + 0 = 1 (Krok 2, kończymy iterację ponieważ
# uzyskaliśmy liczbę 1) Jeżeli w opisanej powyżej procedurze uzyskamy wynik 1, to liczbę N nazywamy
# “jednokwadratową”. Proszę napisać program, który znajduje K-tą liczbę w zadanym przedziale [L, U ],
# która jest jednocześnie jednokwadratowa i pierwsza.

def is_prime(number:int)->bool:
    a = 1
    sqrt = number**(0.5)
    if number < 2:
        return False
    while a <= sqrt:
        a += 1
        if number % a == 0:
            return False
    return True

def check(L:int, U:int, K:int)->int:
    count = 0
    for number in range(L, U+1):
        if is_prime(number):
            sum = number
            while sum != 1 and sum != 4:
                tmp, sum = sum, 0
                while tmp > 0:
                    tmp, digit = divmod(tmp, 10)
                    sum += digit**2
            if sum % 10 == 1:
                count += 1
        if count == K:
            return number
    return 0

print(check(0,100,1))