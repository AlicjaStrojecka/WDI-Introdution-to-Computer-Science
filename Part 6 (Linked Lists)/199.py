# Zadanie 199.
# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję
# do której przekazujemy wskaźnik na początek listy oraz wartość klucza.
# Jeżeli element o takim kluczu występuje w liście należy go usunąć z listy.
# Jeżeli elementu o zadanym kluczu brak jest w liście należy element o
# takim kluczu wstawić do listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def func(p, key) -> Node:
    head = Node(None, p)
    prev = head
    curr = p
    while curr is not None:
        if curr.val == key:
            prev.next = curr.next
            return head.next
        prev, curr = curr, curr.next

    prev.next = Node(key)
    return head.next




