# Zadanie 213.
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję,
# która zwraca wskaźnik do ostatniego elementu przed cyklem.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p) -> Node | None:
    slow, fast = p, p
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    prev, curr = None, p
    while curr != slow:
        slow = slow.next
        prev = curr
        curr = curr.next
    if curr == p:
        return None
    return prev
