# Zadanie 223.
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego.
# Z wnętrza listy usunięto pewną liczbę elementów. Proszę napisać funkcję
# repair(p), (p wskazuje na pierwszy element listy) która uzupełnia listę
# elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego.
# Funkcja powinna zwrócić liczbę wstawionych elementów. Można założyć, że
# lista wejściowa liczy więcej niż 2 elementy.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def nwd(a, b) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def repair(p) -> int:
    prev, curr = p, p.next
    negative = False
    if p.val > p.next.val:
        negative = True
    d = abs(curr.val - prev.val)
    while curr is not None:
        d = nwd(curr.val - prev.val, d)
        prev, curr = curr, curr.next

    prev, curr = p, p.next
    total = 0

    if negative:
        d = -d

    while curr is not None:
        while curr.val - prev.val != d:
            prev.next = Node(prev.val + d, curr)
            prev = prev.next
            total += 1
        prev, curr = curr, curr.next

    return total


