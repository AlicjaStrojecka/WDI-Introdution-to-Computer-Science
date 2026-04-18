# Zadanie 207.
# Elementy w liście są uporządkowane według wartości klucza.
# Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym
# kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p) -> int:
    head = Node(None, p)
    prev, curr = head, p
    total = 0
    while curr is not None:
        start = curr
        count = 1

        while curr.next is not None and curr.next.val == start.val:
            curr = curr.next
            count += 1

        if count > 1:
            prev.next = curr.next
            total += count
        else:
            prev = curr

        curr = curr.next

    return total
