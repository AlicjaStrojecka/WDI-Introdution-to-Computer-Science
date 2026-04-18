# Zadanie 234.
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawiera wartości będące liczbami naturalnymi. Proszę napisać funkcję divide(p),
# (p wskazuje na pierwszy element listy) która rozdziela listę na dwie listy. W pierwszej
# powinny się znaleźć liczby, które są wielokrotnością (co najmniej dwukrotnością) kwadratu
# dowolnego wyrazu ciągu Fibonacciego większego od 1, a w drugiej pozostałe liczby.
# Względny porządek w powstałych listach nie powinien ulec zmianie.
# Funkcja powinna zwrócić wskazania do obu list.

class Node:
    def __init__(self,val, next = None):
        self.val = val
        self.next = next

def is_fib(num) -> bool:
    a, b = 1, 2
    while b*b <= num//2:
        power = b * b
        if num % power == 0:
            return True
        a, b = b, a + b
    return False


def divide(p) -> tuple:
    z1, z2 = Node(None), Node(None)
    t1, t2 = z1, z2
    prev, curr = Node(None, p), p

    while curr is not None:
        prev.next = curr.next
        if is_fib(curr.val):
            t1.next = curr
            t1 = t1.next
        else:
            t2.next = curr
            t2 = t2.next

        curr.next = None
        curr = prev.next

    return z1.next, z2.next
