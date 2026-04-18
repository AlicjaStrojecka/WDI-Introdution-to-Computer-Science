# Zadanie 205.
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

def test(key:int)->bool:
    count = [0, 0]
    while key > 0:
        key, rest = divmod(key, 2)
        count[rest] += 1
    if count[1] % 2 == 1:
        return True
    return False

def func(p)->Node:
    head = Node(None, None, p)
    prev, curr = head, p
    while curr is not None:
        if test(curr.val):
            prev.next = curr.next
            if curr.next is not None:
                curr.next.prev = prev
            curr = curr.next
        else:
            prev, curr = curr, curr.next
    return head.next

