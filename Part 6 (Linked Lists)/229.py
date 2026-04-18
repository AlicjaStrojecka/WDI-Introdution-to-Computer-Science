# Zadanie 229.
# Listy odsyłaczowe budowane są z obiektów zawierających dwa pola: val przechowujące
# liczbę naturalną oraz pole next przechowujące wskaźnik do kolejnego elementu.
# Dane były dwie niepuste listy odsyłaczowe równej długości, każda zawierała rosnący
# ciąg arytmetyczny zaczynający się od wartości 1. Nieudane scalanie tych list
# spowodowało powstanie jednej listy o całkowicie pomieszanej kolejności elementów.
# Proszę napisać funkcję fix(p), która z takiej listy odtwarza dwie listy sprzed
# nieudanego scalania. Do funkcji przekazujemy wskaźnik na scaloną listę, funkcja
# powinna zwrócić dwa wskaźniki na odtworzone listy.
# Na przykład dla listy:
# 9 → 7 → 11 → 3 → 26 → 36 → 13 → 15 → 31 → 21 → 6 → 16 → 1 → 11 → 1 → 5
# Powinny zostać odtworzone listy:
# 1 → 3 → 5 → 7 → 9 → 11 → 13 → 15
# 1 → 6 → 11 → 16 → 21 → 26 → 31 → 36

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def sorting(p) -> Node:
    main = Node(0)
    track = Node(None, main)
    prev, curr = Node(None, p), p

    while curr is not None:
        head, tail = track, track.next  
        prev.next = curr.next
        while tail is not None and curr.val > tail.val:
            head, tail = tail, tail.next
        curr.next = tail
        head.next = curr
        curr = prev.next

    return main.next

def fix(p) -> tuple:
    sorted_p = sorting(p)
    z1 = sorted_p
    z2 = sorted_p.next
    head = z2.next

    z1.next = head
    z2.next = None

    d = head.val - 1

    t1, t2 = z1.next, z2
    t1.next = None

    prev, curr = head, head.next
    while curr is not None:
        prev.next = curr.next
        curr.next = None
        if curr.val - t1.val == d:
            t1.next = curr
            t1 = t1.next
        else:
            t2.next = curr
            t2 = t2.next
        curr = prev.next

    return z1, z2
