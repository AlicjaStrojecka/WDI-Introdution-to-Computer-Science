#Zadanie 24.
#Dane są ciągi: An+1 = √(An ∗ Bn) oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne
#do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Proszę napisać
#program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych

def an(a:float, b:float)->float:
    return (a * b) ** 0.5

def bn(a:float, b:float)->float:
    return (a + b) / 2.0

def lim(num1:int, num2:int)->float:
    curr_a, next_a = num1, 0
    curr_b, next_b = num2, 0
    while curr_a != curr_b:
        next_a, next_b = an(curr_a, curr_b), bn(curr_a, curr_b)
        curr_a, curr_b = next_a, next_b
    return curr_a

print(lim(2,6))