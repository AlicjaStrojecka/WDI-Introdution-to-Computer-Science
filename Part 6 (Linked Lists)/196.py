# Zadanie 196.
# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element
# listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete(head) -> Node:
    prev, curr = head, head.next
    while curr is not None:
            prev.next = curr.next
            prev = prev.next
            if prev is None:
                break
            curr = prev.next

    return head

