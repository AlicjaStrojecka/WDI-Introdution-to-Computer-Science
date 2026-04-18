# Zadanie 197.
# Dana jest niepusta lista reprezentująca liczbę naturalną.
# Kolejne elementy listy przechowują kolejne cyfry.
# Proszę napisać funkcję zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_one(p) -> Node:
    def rec(head) -> int:
        tail = head
        if tail.next is None or rec(tail.next) == 1:
            tail.val += 1
            if tail.val == 10:
                tail.val = 0
                if tail != p:
                    return 1
            return 0
    carry = rec(p)
    if carry == 1:
        p = Node(1, p)
    return p




