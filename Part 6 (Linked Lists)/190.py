# Zadanie 190. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# • inicjalizującą tablicę,
# • zwracającą wartość elementu o indeksie n,
# • podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def initialize(p) -> Node:
    head = curr = Node(None)
    ind = 0
    while p != None:
        if p.val != None:
            curr.next = Node((ind, p.val))
            curr = curr.next
        p = p.next
        ind += 1
    return head.next

def get_value(p, n) -> Node | None:
    while p != None and p.val[0] < n:
        p = p.next
    return p.val[1] if p != None and p.val[0] == n else None

def change_value(p, n, value) -> Node:
    head = Node(None, p)
    prev, curr = head, p
    while curr != None and curr.val[0] < n:
        prev, curr = curr, curr.next

    if value == None:
        if curr != None and curr.val[0] == n:
            prev.next = curr.next
    elif curr != None and curr.val[0] == n:
        curr.val = (n, value)
    else:
        prev.next = Node((n, value), curr)

    return head.next

