# Zadanie 198.
# Liczby naturalne reprezentowane jak poprzednim zadaniu.
# Proszę napisać funkcję dodającą dwie takie liczby.
# W wyniku dodawania dwóch liczb powinna powstać nowa lista.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_two(p, q) -> Node:
    def reverse_list(node):
        prev, curr = None, node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev
    p, q = reverse_list(p), reverse_list(q)
    curr, head = Node(0)
    carry = 0

    while p or q or carry:
        p_val = p.val if p else 0
        q_val = q.val if q else 0

        total = p_val + q_val + carry
        carry, value = divmod(total, 10)

        curr.next = Node(value)
        curr = curr.next

        if p:
            p = p.next
        if q:
            q = q.next

    return reverse_list(head.next)




