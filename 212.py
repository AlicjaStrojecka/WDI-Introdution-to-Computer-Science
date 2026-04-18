# Zadanie 212.
# Dana jest lista, która zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def count(p)->int:
    slow, fast = p, p
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    start = p
    while start != slow:
        start = start.next
        slow = slow.next

    count = 0
    node = p
    while node != slow:
        node = node.next
        count += 1

    return count
