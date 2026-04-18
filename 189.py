#Zadanie 189.
# Proszę zaimplementować zbiór mnogościowy liczb naturalnych
# korzystając ze struktury listy odsyłaczowej:
# • czy element należy do zbioru
# • wstawienie elementu do zbioru
# • usunięcie elementu ze zbioru

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def contains(head, target) -> bool:
    while head != None:
        if head.val == target:
            return True
        head = head.next
    return False

def add(head, value) -> Node:
    return Node(value, head) if not contains(head, value) else head

def delete(head, target) -> Node:
    if head.val == target:
        return head.next

    prev, curr = Node(0, head), head
    while curr != None:
        if curr.val == target:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next

    return head

