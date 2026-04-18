#Zadanie 21.
#Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N,
#dla którego ciąg osiąga wartość 1 dokładnie po N krokach.

def count(n:int)->int:
    steps = 0
    m = n
    while m != 1:
        m = ((m % 2) * (3 * m + 1)) + ((1 - (m % 2)) * m / 2)
        steps +=1
    return steps

def most_steps(N:int)->int:
    min = [N, 0]
    for n in range(2, 10001):
        if min[0] == count(n):
            min[1] = n
    return min

print(most_steps(233))