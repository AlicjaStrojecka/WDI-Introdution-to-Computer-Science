# Zadanie 206.
# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p) -> Node:
    head = Node(None,p)
    pprev = head
    while p is not None:
        prev, curr = p, p.next
        found = False
        while curr is not None:
            if p.val == curr.val:
                prev.next = curr.next
                curr = curr.next
                found = True
            else:
                prev, curr = curr, curr.next
        if found:
            pprev.next = p.next
            p = p.next
        else:
            pprev, p = p, p.next
    return head.next

