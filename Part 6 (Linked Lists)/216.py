# Zadanie 216.
# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne.
# W pierwszej liście liczby są posortowane rosnąco, a w drugiej nie.
# Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
# listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def check(node)->bool:
    while node is not None and node.next is not None:
        if node.val >= node.next.val:
            return False
        node = node.next
    return True

def func(p, q)->int:
    if check(p):
        main, sub = p, q
    else:
        main, sub = q, p

    subhead = Node(None, sub)
    mprev, mcurr = Node(None, main), main
    total = 0

    while mcurr is not None:
        sprev, scurr = subhead, sub

        while scurr is not None:
            if scurr.val == mcurr.val:
                sprev.next = scurr.next
                break
            else:
                sprev = scurr
                scurr = scurr.next

        if scurr is not None:
            if scurr == sub:
                subhead.next = sub.next
                sub = sub.next
            mprev.next = mcurr.next
            mcurr = mcurr.next
            total += 2
        else:
            mprev = mcurr
            mcurr = mcurr.next

    return total



