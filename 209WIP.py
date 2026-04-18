# Zadanie 209.
# Kolejne elementy listy o zwiększającej się wartości pola val
# nazywamy podlistą rosnącą. Proszę napisać funkcję, która usuwa z
# listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def remove(p: Node) -> Node:
    head = Node(None, p)
    before = head
    start, end = head, head
    prev, curr = p, p.next
    highest = [0, 0]
    while prev is not None:
        count = 1
        while curr is not None:
            if curr.val > prev.val: #wartosci rosna
                count += 1
            elif count > 1 or curr.next == None: #przestaly rosnac
                if count > highest[0]: #gdy unikalne val
                    highest[0] = count
                    highest[1] = 1
                    start = before
                    end = curr
                elif count == highest: #gdy sie powtarza
                    highest[1] += 1
                count = 1
            else:
                before = prev
                prev, curr = curr, curr.next
    if highest[1] == 1:
        start.next = end
    return head.next






