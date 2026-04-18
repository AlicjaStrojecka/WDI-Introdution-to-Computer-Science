#Zadanie 6.
#Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
#Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2

def root(num: int)->int:
    sum = 0
    index = 0
    while sum <= num:
        sum += 1+2*index
        index += 1
    return index-1

print(root(25))