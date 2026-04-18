# Zadanie 203.
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def test(key:int) -> bool:
    count = [0,0,0]
    while key > 0:
        key, rest = divmod(key, 3)
        count[rest] += 1
    if count[1] > count[2]:
        return True
    return False

def func(p) -> Node:
    head = Node(None, p)
    prev, curr = head, p
    while curr is not None:
        if test(curr.val):
            prev.next = curr.next
            curr = curr.next
        else:
            prev, curr = curr, curr.next

    return head.next

