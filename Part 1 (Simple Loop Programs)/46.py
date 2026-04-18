# Zadanie 46.
# Dane są dwie liczby naturalne, m i n. Proszę napisać program, który wyznacza
# sumę n kolejnych cyfr po przecinku rozwinięcia dziesiętnego liczby sqrt(m)

def sum(m:int, n:int)->int:
    expansion = m**(0.5) * 10**(n)
    sum = 0
    for i in range(n):
        print(expansion)
        expansion, digit = divmod(expansion, 10)
        sum += digit
    return sum

print(sum(7,106))