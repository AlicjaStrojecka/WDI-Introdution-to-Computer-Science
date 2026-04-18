#Zadanie 17.
#Proszę napisać program wyznaczający najmniejszą wspólną
#wielokrotność 3 zadanych liczb naturalnych.

def nwd(a:int, b:int)->int:
    while b > 0:
        a, b = b, a % b
    return a

def nww(a:int, b:int)->int:
    return ((a*b)//nwd(a,b))

print(nww(nww(15,25),25))