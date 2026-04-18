# Zadanie 215.
# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna, - funkcja rekurencyjna.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def sort(p, q) -> Node:
    head = Node(None)
    curr = head

    while p is not None and q is not None:
        if p.val < q.val:
            curr.next = p
            p = p.next
        else:
            curr.next = q
            q = q.next
        curr = curr.next

    if p is not None:
        curr.next = p
    if q is not None:
        curr.next = q

    return head.next

