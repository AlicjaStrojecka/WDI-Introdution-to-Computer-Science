# Zadanie 231.
# Lista odsyłaczowa zbudowana jest z obiektów zawierających dwa pola: val przechowujące
# liczbę naturalną oraz pole next przechowujące wskaźnik do kolejnego elementu.
# Dana była niepusta lista odsyłaczowa, która zawierała rosnący ciąg wartości val.
# Przez pomyłkę spójny fragment tej listy liczący 6 elementów został przeniesiony w
# inne miejsce w liście. Proszę napisać funkcję fix(p), która naprawia taką listę,
# tak aby przywrócić rosnący porządek elementów. Do funkcji przekazujemy wskaźnik na
# listę, funkcja powinna zwrócić dwa wskaźniki na naprawioną listę.
# Przykładowe ”zepsute” listy:
# 2 → 3 → 23 → 29 → 5 → 7 → 11 → 13 → 17 → 19 → 31 → 37 → 41 → 43 → 47 → 53
# przeniesiony fragment 5 do 19
# 17 → 19 → 23 → 29 → 31 → 37 → 41 → 2 → 3 → 5 → 7 → 11 → 13 → 43 → 47 → 53
# przeniesiony fragment 2 do 13
# Powinny zostać przekształcone do listy:
# 2 → 3 → 5 → 7 → 11 → 13 → 17 → 19 → 23 → 29 → 31 → 37 → 41 → 43 → 47 → 53

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def fix(p) -> Node:
    head = Node(-float('inf'), p)
    prev, curr = p, p.next

    broken_prev = None
    while curr is not None:
        if curr.val < prev.val:
            broken_prev = prev
            break
        else:
            prev, curr = curr, curr.next

    if broken_prev is None:
        return head.next

    six_start = broken_prev.next
    six_end = six_start

    for _ in range(5):
        six_end = six_end.next

    broken_prev.next = six_end.next
    six_end.next = None

    prev, curr = head, head.next

    while curr is not None and curr.val < six_start.val:
        prev, curr = curr, curr.next

    prev.next = six_start
    six_end.next = curr

    return head.next

