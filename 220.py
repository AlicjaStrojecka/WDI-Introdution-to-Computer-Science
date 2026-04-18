# Zadanie 220.
# Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
# liście ułożone są według rosnących potęg. Proszę napisać funkcję
# obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany
# reprezentowane są przez wyżej opisane listy. Procedura powinna zwracać
# wskaźnik do nowo utworzonej listy reprezentującej wielomian wynikowy.
# Listy wejściowe powinny pozostać niezmienione.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def main(x, y) -> Node:
    head = tail = Node(None)
    #eq = x - y
    while x is not None and y is not None:
        tail.next = Node(x.val - y.val)
        tail = tail.next
        x, y = x.next, y.next
    while x is not None:
        tail.next = Node(x.val)
        tail = tail.next
        x = x.next
    while y is not None:
        tail.next = Node(-(y.val))
        tail = tail.next
        y = y.next
    return head.next


