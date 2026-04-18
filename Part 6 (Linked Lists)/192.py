# Zadanie 192.
# Proszę napisać funkcję, która dla podanej listy odsyłaczowej
# odwraca kolejność jej elementów.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def revert(head):
    prev, curr = None, head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    return prev


