# Zadanie 232.
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawierała liczby naturalne stanowiące kolejne wyrazy ciągu An spełniającego
# warunek An = An−1 + An−2. Z wnętrza listy usunięto pewną liczbę elementów, ale:
# 1. Pierwszy i ostatni element ciągu pozostały w liście,
# 2. Co najmniej trzy kolejne elementy ciągu znajdują się w liście.
# Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która uzupełnia
# listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu An.
# Funkcja powinna zwrócić liczbę wstawionych elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def repair(p) -> int:
    head = Node(0, p)
    total = 0
    prev, curr = p, p.next
    an1 = an2 = None
    while curr.next is not None:
        if curr.next.val == curr.val + prev.val:
            an2 = curr.val
            an1 = prev.val
            break
        else:
            prev, curr = curr, curr.next

    if an1 is None or curr.next is None:
        return 0

    while an1 != p.val:
        an1, an2 = an2 - an1, an1

    prev, curr = p, p.next
    if curr.val != an2:
        new_node = Node(an2, curr)
        prev.next = new_node
        curr = new_node
        total += 1

    while curr.next is not None:
        amount = prev.val + curr.val
        if amount != curr.next.val:
            new_node = Node(amount, curr.next)
            curr.next = new_node
            total += 1
        else:
            prev, curr = curr, curr.next

    return total