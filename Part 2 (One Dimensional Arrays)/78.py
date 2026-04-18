# Zadanie 78.
# Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy
# w tablicy zachodzi następujący warunek: „wszystkie elementy, których indeks
# jest elementem ciągu Fibonacciego są liczbami złożonymi, a wśród pozostałych
# przynajmniej jedna jest liczbą pierwszą”

def is_fib(index:int)->bool:
    curr, next = 0, 1
    while curr <= index:
        if next == index:
            return True
        curr, next = next, curr + next
    return index == 0

def is_prime(number:int)->bool:
    if number == 0 or number == 1:
        return False
    sqrt = int(number ** (0.5))
    divider = 2
    while divider <= sqrt:
        if number % divider == 0:
            return False
        divider += 1
    return True

def main(T:list)->bool:
    length = len(T)
    all_fib = True
    non_fib = False
    for index, value in enumerate(T):
        if is_fib(index):
            if is_prime(value):
                all_fib = False
        else:
            if is_prime(value):
                non_fib = True
    return non_fib and all_fib


