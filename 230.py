# Zadanie 230.
# Dana jest lista, zbudowana z elementów zawierających pola val i next,
# której węzły przechowują parami różne liczby naturalne.
# Proszę napisać funkcję sort(p), która porządkuje elementy listy wskazywanej przez
# wskaźnik p, według niemalejącej liczby jedynek w kluczu, zapisanym w systemie o
# podstawie 2, a w przypadku identycznej liczby jedynek liczba mniejsza powinna
# poprzedzać większą. Funkcja powinna zwrócić wskazanie do uporządkowanej listy.
# Na przykład dla listy zawierającej elementy: 31 7 13 5 11 3 2 1 32
# uporządkowana lista wygląda następująco: 1 2 32 3 5 7 11 13 31

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def base(num:int) -> int:
    new = 0

    while num > 0:
        if num % 2 == 1:
            new += 1
        num //= 2
    return new


def sort(p) -> Node:
    main = Node(None, p)

    track = Node(0)
    prev, curr = main, main.next

    while curr is not None:
        #odpinamy chopaka
        prev.next = curr.next
        #resetujemy pozycje head i tail, liczymy ilość jedynek w curr.val
        head, tail = track, track.next
        count = base(curr.val)

        while tail is not None:
            #ilość jedynek w aktualnym tail
            tcount = base(tail.val)
            #idziemy dalej póki tail jest mniejsze LUB póki jedynek jest takie samo a tail.val jest mniejsze
            if tcount < count or (tcount == count and tail.val < curr.val):
                head, tail = tail, tail.next
            else:
                break

        head.next = curr
        curr.next = tail

        curr = prev.next

    return track.next
