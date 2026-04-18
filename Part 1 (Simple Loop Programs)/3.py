#Zadanie 3.
#Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

def fib():
    curr, next = 0, 1
    while curr < 1000000 :
        print(curr)
        next, curr = curr+next, next

fib()