# Zadanie 211.
# Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def count(p) -> int:
    slow, fast = p, p
    while True:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    count = 1
    curr = slow.next
    while curr != slow:
        count += 1
        curr = curr.next
    return count

