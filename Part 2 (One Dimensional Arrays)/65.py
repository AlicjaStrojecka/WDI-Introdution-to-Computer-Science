# Zadanie 65.
# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z
# takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def count(number:int)->list:
    amount = [0]*10
    while number > 0:
        amount[number % 10] += 1
        number //= 10
    return amount

def check(num1:int, num2:int)->bool:
    if count(num1) == count(num2):
        return True
    return False

print(check(1100, 11000))