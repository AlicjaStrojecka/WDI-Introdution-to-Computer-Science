# Zadanie 194.
# Proszę napisać funkcję wstawiającą na koniec listy nowy element.
# Do funkcji należy przekazać wskazanie na pierwszy element listy
# oraz wstawianą wartość.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add(head, value) -> Node:
    tail = head
    new_node = Node(value)
    while tail.next is not None:
        tail = tail.next
    tail.next = new_node

    return head
