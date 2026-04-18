# Zadanie 43.
# Proszę napisać funkcję, która zwraca wartość True gdy dwie liczby są
# zbudowane z tych samych cyfr (na przykład: 123 i 231, 5749 i 4597) i
# wartość False w przeciwnym przypadku.

def check(number:int, digit:int)->bool:
    occur = 0
    while number > 0:
        number, d = divmod(number, 10)
        if d == digit:
            occur += 1
    return occur


def main(num1:int, num2:int)->bool:
    for i in range(10):
        if check(num1, i) != check(num2, i):
            return False
    return True

print(main(124,321))