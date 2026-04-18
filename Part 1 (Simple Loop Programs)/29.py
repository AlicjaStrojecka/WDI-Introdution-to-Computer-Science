#Zadanie 29.
#Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn
#dwóch liczb o najmniejszej różnicy. Na przykład: 30 = 5 ∗ 6, 120 = 10 ∗ 12.

def mult(number:int)->None:
    max = int((number ** 0.5)//1)
    for i in range(max, 0, -1):
        if number % i == 0:
            print(f"{number} = {i} * {number//i}")
            break
    return

mult(8)