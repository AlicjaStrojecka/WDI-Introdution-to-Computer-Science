# Zadanie 214.
# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera
# się w drugiej. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wartość logiczną.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def length(node)->int:
    leng = 0
    while node is not None:
        node = node.next
        leng += 1
    return leng

def check(p, q)->bool:
    if length(p) >= length(q):
        main, sub = p, q
        subhead = q
    else:
        main, sub = q, p
        subhead = p

    while main is not None:
        while main.val == sub.val:
            main = main.next
            sub = sub.next
            if sub is None:
                return True
        else:
            if sub == subhead:
                main = main.next
            else:
                sub = subhead
    return False