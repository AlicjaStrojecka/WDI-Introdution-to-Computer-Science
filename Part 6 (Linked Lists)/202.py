# Zadanie 202.
# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p) -> Node:
    head = Node(None, p)
    prev, curr = head, p
    while curr is not None and curr.next is not None:
        if curr.next.val % prev.next.val == 0:
            prev.next = curr.next
            curr = curr.next
        else:
            prev, curr = curr, curr.next

    return head.next

