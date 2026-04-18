#Zadanie 1.
#Trójką prostokątny o bokach wyrażonych liczbami naturalnymi nazywamy Pitagorejskim.
#Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość
#przekątnej jest mniejsza od liczby N wprowadzonej z klawiatury.

def pitagoras(N)->int:
    for a in range (1,N):
        for b in range (a,N):
            for c in range (b,N):
                if a*a + b*b == c*c:
                    print(a,b,c)

pitagoras(6)