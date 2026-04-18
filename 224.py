# Zadanie 224.
# Dana jest definicja klasy, której obiekty stanowią elementy listy:
# class Node
# ..def init(self,val):
# ....self.val = val
# ....self.next = None
# Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o
# uporządkowanych rosnąco elementach. Proszę napisać funkcję iloczyn(z1,z2,z3),
# która przekształca 3 listy (zbiory) z1,z2,z3 w jedną listę (zbiór) zawierającą
# elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
# wskazanie do listy wynikowej

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def iloczyn(z1, z2, z3) -> Node:
    head = tail = Node(None)

    while z1 is not None and z2 is not None and z3 is not None:
        if z1.val == z2.val == z3.val:
            tail.next = Node(z1.val)
            tail = tail.next
            z1, z2, z3 = z1.next, z2.next, z3.next
        else:
            high = max(z1.val, z2.val, z3.val)

            while z1 is not None and z1.val < high:
                z1 = z1.next
            while z2 is not None and z2.val < high:
                z2 = z2.next
            while z3 is not None and z3.val < high:
                z3 = z3.next

    return head.next




