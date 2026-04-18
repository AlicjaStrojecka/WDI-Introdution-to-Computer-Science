# Zadanie 221.
# Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
# od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
# cyklicznej, na przykład: bartek -> leszek -> marek -> ola -> zosia.
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do
# listy napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
# wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
# logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
# elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def main(cycle, text:str) -> tuple:
    head = cycle
    prev, curr = head, head.next
    first = text[0]
    last = text[-1]

    while True:
        if prev.val[-1] < first and last < curr.val[0]:
            prev.next = Node(text, curr)
            return True, prev.next

        if curr == head:
            return False, cycle

        prev, curr = curr, curr.next

