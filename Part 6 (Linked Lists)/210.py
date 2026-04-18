# Zadanie 210.
# Dana jest lista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def check(head) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
