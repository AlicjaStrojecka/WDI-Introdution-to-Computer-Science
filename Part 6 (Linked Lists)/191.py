# Zadanie 191.
# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę.
# Do funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna
# zwrócić wskazanie do scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną,
# a następnie jako funkcję rekurencyjną.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

def iteration(p, q)-> Node:
    head = tail = Node(0)
    while p != None and q != None:
        if p.val < q.val:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    tail.next = p if p != None else q
    return head.next