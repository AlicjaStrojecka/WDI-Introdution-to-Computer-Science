# Zadanie 225.
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init (self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję
# repair(p), (p wskazuje na pierwszy element listy) która przekształca listę
# tak aby liczby parzyste znalazły się na końcu listy. Funkcja powinna zwrócić
# wskazanie na przekształconą listę. Można założyć, że lista wejściowa liczy
# więcej niż 2 elementy.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def repair(p):
    main = Node(None, p)
    head = tail = Node(None)
    prev, curr = main, p

    while curr is not None:
        if curr.val % 2 == 0:
            prev.next = curr.next
            curr.next = None
            tail.next = curr
            curr = prev.next
            tail = tail.next
        else:
            prev, curr = curr, curr.next

    if head.next is not None:
        prev.next = head.next

    return main.next



