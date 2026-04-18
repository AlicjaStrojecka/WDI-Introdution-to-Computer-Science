# Zadanie 200.
# Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
# jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
# leksykograficznie. Proszę napisać stosowne definicje typów oraz
# funkcję dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik
# do listy oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną
# wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert(p, text) -> bool:
    curr = p
    if text < curr.val:
        p = Node(text, curr)
        return True
    while curr is not None:
        if curr.val == text: return False
        if curr.val < text:
            if curr.next is None:
                curr.next = Node(text)
                return True
            elif curr.next.val > text:
                text_node = Node(text, curr.next)
                curr.next = text_node
                return True
        curr = curr.next
    return False
