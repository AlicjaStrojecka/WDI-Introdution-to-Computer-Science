# Zadanie 83.
# Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000.
# Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy,
# dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz.
# Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.

def factorize(number:int)->set:
    prime = 2
    sqrt = number**(0.5)
    factors = set()
    while prime <= sqrt:
        while number % prime == 0:
            factors.add(prime)
            number //= prime
        prime += 1
    if number > 1:
        factors.add(number)
    return factors


def main(table:list)->int:
    used = set()
    left = 0
    best = 0
    length = len(table)
    for right in range(length):
        primes = factorize(table[right])

        while any(p in used for p in primes):
            for q in factorize(table[left]):
                used.remove(q)
            left += 1

        used |= primes

        best = max(best, right - left + 1)

    return best
