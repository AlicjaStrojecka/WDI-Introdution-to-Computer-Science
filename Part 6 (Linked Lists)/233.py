# Zadanie 233.
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val):
# ....self.val = val
# ....self.next = None
# Lista zawierała liczby naturalne stanowiące kolejne wyrazy rosnącego ciągu arytmetycznego.
# Pewien fragment listy zastąpiono jego rewersem. Na szczęście pierwszy i ostatni element
# ciągu pozostały na swoich miejscach. Proszę napisać funkcję repair(p), (p wskazuje na
# pierwszy element listy) która przywraca listę do stanu początkowego.
# Funkcja powinna zwrócić długość odwróconego fragmentu.
# Na przykład:
# listę 3,11,9,7,5,13,15,17,19 należy przekształcić w listę 3,5,7,9,11,13,15,17,19

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# an = a1 + r(n-1)
# an - a1 = r(n-1)
# 16 = 2 * 8
def find(p) -> int:
    first = p.val
    curr = p
    elements = 0
    while curr.next is not None:
        curr = curr.next
        elements += 1
    last = curr.val
    r = (last - first) // elements
    return r

def repair(p) -> int:
    r = find(p)
    prev, curr = p, p.next
    seq = 0
    while curr is not None:
        if prev.val + r == curr.val:
            prev, curr = curr, curr.next
        else:
            ## czyli z r robi się -r
            break

    if curr is None:
        return seq

    link_start = prev
    seq_start = prev.next
    prev, curr = curr, curr.next
    seq = 2

    while curr is not None and curr.val == prev.val - r:
        prev, curr = curr, curr.next
        seq += 1

    seq_end = prev
    link_end = curr

    link_start.next, seq_end.next = None, None

    def rec(node) -> Node:
        if node is seq_end:
            return node
        new_head = rec(node.next)
        node.next.next = node
        node.next = None
        return new_head

    seq_start = rec(seq_start)

    link_start.next = seq_end
    seq_start.next = link_end

    return seq
