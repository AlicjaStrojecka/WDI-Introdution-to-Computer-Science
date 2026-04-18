#Zadanie 188. Zliczanie elementów łańcucha

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def count(p: Node | None) -> int:
    total = 0
    while p != None:
        total += 1
        p = p.next
    return total