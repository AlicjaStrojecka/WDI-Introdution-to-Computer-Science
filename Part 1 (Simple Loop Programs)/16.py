#Zadanie 16.
# roszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych.

def nwd(a:int, b:int)->int:
    while b > 0:
        a, b = b, a%b
    return a

print(nwd(nwd(20,40),20))
