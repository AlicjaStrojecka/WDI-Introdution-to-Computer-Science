# Zadanie 218.
# Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy.
# Elementy w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują
# w przypadkowej kolejności. Proszę napisać funkcję, która z dwóch takich list stworzy jedną,
# w której uporządkowane elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić wskazanie
# na listę wynikową. Na przykład dla list:
# 2 → 3 → 5 → 7 → 11
# 8 → 2 → 7 → 4
# powinna pozostać lista:
# 2 → 3 → 4 → 5 → 7 → 8 → 11

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def func(p, q) -> Node:
    head = Node(None, p)

    while q is not None:
        prev, curr = head, head.next
        inserted = False

        while curr is not None:
            if curr.val == q.val:
                inserted = True
                break

            if prev.val is None and q.val < curr.val:
                new = Node(q.val, curr)
                prev.next = new
                inserted = True
                break

            elif prev.val < q.val < curr.val:
                new = Node(q.val, curr)
                prev.next = new
                inserted = True
                break

            else:
                prev, curr = curr, curr.next

        if not inserted:
            prev.next = Node(q.val)

        q = q.next

    return head.next














