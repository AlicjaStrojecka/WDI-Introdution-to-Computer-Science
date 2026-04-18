# Zadanie 85.
# Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego
# wartości sqrt(2). Program powinien działać poprawnie dla n < 100.

def main(N:int)->int:
    shift = 2*N
    square = (2*(10**shift))**(0.5)
    print(int((square % 10)//1))

main(17)