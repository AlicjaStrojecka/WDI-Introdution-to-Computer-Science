#Zadanie 20.
#Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
#Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1.
#Proszę napisać program, który znajdzie wyraz początkowy z przedziału
#2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def count(n:int)->int:
    steps = 0
    m = n
    while m != 1:
        m = ((m % 2) * (3 * m + 1)) + ((1 - (m % 2)) * m / 2)
        steps +=1
    return steps

def most_steps()->int:
    most = [1, 0]
    for n in range(2, 10001):
        if most[0] < count(n):
            most = [count(n), n]
    return most

print(most_steps())



























