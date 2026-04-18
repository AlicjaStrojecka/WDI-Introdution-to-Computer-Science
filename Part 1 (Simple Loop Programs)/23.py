#Zadanie 23.
#Proszę napisać program wyznaczający wartość liczby e korzystając z
#zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ...

def factorial(n:int)->float:
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return (1/fact)

def euler():
    prev_e, curr_e, index = 0, 1, 1
    while curr_e != prev_e:
        prev_e = curr_e
        curr_e += factorial(index)
        index += 1
    return curr_e

print(euler())