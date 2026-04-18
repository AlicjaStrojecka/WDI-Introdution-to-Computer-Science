# Zadanie 217.
# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne.
# W obu listach liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą
# z każdej listy liczby nie występujące w drugiej. Do funkcji należy przekazać
# wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych
# elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p, q)->int:
    total = 0
    pprev = Node(None, p)
    qprev = Node(None, q)
    while p is not None and q is not None:
        if p.val == q.val:
            p = p.next
            q = q.next
            pprev = pprev.next
            qprev = qprev.next
        elif p.val > q.val:
            qprev.next = q.next
            q = q.next
            total += 1
        else:
            pprev.next = p.next
            p = p.next
            total += 1

    while p is not None:
        pprev.next = p.next
        p = p.next
        total += 1

    while q is not None:
        qprev.next = q.next
        q = q.next
        total += 1

    return total






