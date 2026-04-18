# Zadanie 208.
# Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
# napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien
# zostać zredukowany do listy: [13,19] [2,6] [7,12]

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def reduce(p) -> Node:
    imp = p
    while imp is not None:
        prev = imp
        curr = imp.next
        while curr is not None:
            if not (imp.val[1] < curr.val[0] or curr.val[1] < imp.val[0]): #czesc wspolna
                imp.val[0] = min(imp.val[0], curr.val[0])
                imp.val[1] = max(imp.val[1], curr.val[1])
                prev.next = curr.next
                curr = prev.next
            else:
                prev, curr = curr, curr.next
        imp = imp.next
    return p



