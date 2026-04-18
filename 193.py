# Zadanie 193.
# Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej
# do 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe
# listy należy połączyć w jedną listę odsyłaczową, która jest
# posortowana niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def divide(head) -> Node:
    heads = []
    tails = []

    for _ in range(10):
        sentinel = Node(0)
        heads.append(sentinel)
        tails.append(sentinel)

    while head is not None:
        last_digit = abs(head.val) % 10
        next_node = head.next
        head.next = None
        tails[last_digit].next = head
        tails[last_digit] = head

        head = next_node

    result_tail = result_sentinel = Node(0)

    for i in range(10):
        if heads[i].next is not None:
            result_tail.next = heads[i].next
            result_tail = tails[i]

    return result_sentinel.next



