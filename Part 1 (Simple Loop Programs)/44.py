# Zadanie 44.
# Dla pewnej N-cyfrowej liczby naturalnej obliczono sumę N-tych potęg cyfr tej liczby otrzymując
# kolejną liczbę N-cyfrową. Na przykład dla liczb: 354, 543, 600, ... suma ta wynosi 216.
# Niestety pierwotna liczba zaginęła ale wiadomo, że była to największa z możliwych takich liczb.
# Proszę napisać program, który na podstawie zachowanej sumy wyznaczy pierwotną liczbę

def check(digit_sum:int)->int:
    length = len(str(digit_sum))
    max = 10 ** (length) - 1
    min = max // 10
    for number in range(max, min, -1):
        sum_of_digits = 0
        power = 0
        while sum_of_digits < digit_sum:
            sum_of_digits = 0
            in_number = number
            while in_number > 0:
                in_number, digit = divmod(in_number, 10)
                sum_of_digits += digit**(power)
            power += 1
        if sum_of_digits == digit_sum:
            return number
    return number


def sum(number:int)->int:
    length = len(str(number))
    sum_of_digits = 0
    power = 0
    while sum_of_digits < 10**(length-1):
        sum_of_digits = 0
        in_number = number
        for i in range(length):
            in_number, digit = divmod(in_number, 10)
            sum_of_digits += digit**(power)
        power += 1
    return sum_of_digits

#print(sum(354))
print(check(216))