#Zadanie 22.
#Proszę napisać program wyznaczający wartość do której zmierza iloraz
#dwóch kolejnych wyrazów ciągu Fibonacciego. Wyznaczyć te ilorazy dla
#różnych wartości dwóch początkowych wyrazów ciągu.

def fib(index:int)->float:
    prev, curr = 0, 1
    n = 0
    while n < index:
        prev, curr = curr, prev + curr
        n += 1
    return curr/prev

def quo():
    backup = 0
    index = 1
    current = fib(index)
    while backup != current:
        backup = current
        index += 1
        current = fib(index)
    return backup

print(quo())