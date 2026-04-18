# Zadanie 201.
# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p) -> Node:
    prev, curr = p, p.next
    while curr is not None:
        if curr.val < prev.val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev, curr = curr, curr.next
    return p

