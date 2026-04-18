#Zadanie 31.
#Proszę napisać program, który oblicza pole figury pod wykresem funkcji
#y = 1/x w przedziale od 1 do k, metodą prostokątów.

def pole(k:int)->int:
    suma = 0
    for i in range(1,k+1):
        suma += i**(-1)
        print(suma)
    return suma
pole(3)
