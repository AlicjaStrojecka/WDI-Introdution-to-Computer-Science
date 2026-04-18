# Zadanie 64.
# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

def base_change(number:int, base:int)->list:
    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    in_number = number
    length = 0
    while in_number > 0:
        in_number //= base
        length += 1
    new_number = [0]*length
    for index in range(length-1 , -1, -1):
        new_number[index] = tab[number % base]
        number //= base
    return new_number

def convert(number:int)->None:
    for base in range(2,17):
        print(base, base_change(number, base))

convert(15)



