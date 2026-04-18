# Zadanie 195.
# Proszę napisać funkcję usuwającą ostatni element listy.
# Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete(head) -> Node:
    if head is None or head.next is None:
        return None

    tail = head
    while tail.next.next is not None:
        tail = tail.next

    tail.next = None
    return head
