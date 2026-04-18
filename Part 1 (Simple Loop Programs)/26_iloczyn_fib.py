#Zadanie 26.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
#czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

def fib(index:int)->int:
    prev, curr = 0, 1
    n = 0
    while n < index:
        prev, curr = curr, prev + curr
        n += 1
    return prev

def check(number:int)->bool:
    for i in range(0, number+1):
        for j in range(i+1, number+2):
            if fib(i) * fib(j) == number:
                return True
    return False

if check(7):
    print("True")
else:
    print("False")