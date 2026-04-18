#Zadanie 10.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający
#na pytanie, czy liczba ta jest iloczynem dowolnych dwóch kolejnych
#wyrazów ciągu Fibonacciego

def fib(n:int)->int:
    curr, next = 0, 1
    i = 0
    while i <= n:
        curr, next = next, curr+next
        i += 1
    return curr

def is_mult(n)->bool:
    result = False
    j = 0
    while j <= n:
        if n == fib(j-1)*fib(j):
            result = True
            break
        j += 1
    return result

def check(n)->str:
    if is_mult(n):
        print("The value is a multiplication of 2 next fibonacci numbers")
    else:
        print("it's not")

check(15)