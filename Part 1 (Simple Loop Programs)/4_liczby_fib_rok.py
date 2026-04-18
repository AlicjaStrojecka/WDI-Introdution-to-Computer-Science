#Zadanie 4.
#Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
#analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
def fib(rok):
    for a in range(0,rok):
        for b in range(1,rok):
            curr = a
            next = b
            while next < rok:
                next, curr = curr+next, next
                #print(curr, next)
                if next + curr == rok:
                    print(a,b)
                    return

fib(2584)