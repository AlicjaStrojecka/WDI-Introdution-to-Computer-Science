# Zadanie 204.
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def test(key:int) -> bool:
    count = [0 for _ in range(8)]
    while key > 0:
        key, rest = divmod(key, 8)
        count[rest] += 1
    if count[5] % 2 == 0:
        return True
    return False

def func(p) -> Node:
    head = p
    prev, curr = head, p.next
    while curr is not None:
        if test(curr.val):
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next
        else:
            prev, curr = curr, curr.next
    return head

