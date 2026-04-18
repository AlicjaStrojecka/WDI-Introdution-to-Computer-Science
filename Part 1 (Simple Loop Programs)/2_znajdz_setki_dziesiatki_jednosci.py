#Zadanie 2.
#Proszę napisać program odnajdujący cyfry a, b, c w działaniu: abc + abc + abc = bbb.

def find(number)->int:
# 3*(100a + 10b + c) = 111b
    a = number // 100
    b = number // 10
    c = number % 10
    for a in range (4): #maks. liczba setek to 3 ponieważ (999 // 100) // 3 = 3
        for b in range (9):
            for c in range (9):
                if 3*(100*a + 10*b + c) == number:
                    print(a,b,c)

find()