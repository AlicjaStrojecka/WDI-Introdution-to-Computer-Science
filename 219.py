# Zadanie 219.
# Proszę napisać funkcję, która rozdziela listę na dwie listy.
# Pierwsza powinna zawierać klucze parzyste dodatnie, drugi klucze
# nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci.
# Do funkcji należy przekazać wskaźniki na listę z danymi oraz wskaźniki
# na listy wynikowe. Funkcja powinna zwrócić liczbę usuniętych elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def sort(p) -> tuple:
    even = Node(None)
    odd = Node(None)
    total = 0

    while p is not None:
        value = p.val

        if value > 0 and value % 2 == 0:
            new = Node(value)
            even.next = new
            even = even.next

        elif value < 0 and value % 2 == 1:
            new = Node(value)
            odd.next = new
            odd = odd.next

        else:
            total += 1

        p = p.next

    return total

