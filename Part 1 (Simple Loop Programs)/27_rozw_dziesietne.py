#Zadanie 27.
#Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie
#dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

def ten(a:int, b:int, i:int):
    return (a * (10 ** i) // b) % 10

def exp(a:int, b:int, n:int)->float:
    print(f"{a // b}.", end ='')
    for i in range (1, n):
        fraction = ten(a, b, i)
        print(fraction, end ='')
    return fraction

print(exp(22, 7, 10))