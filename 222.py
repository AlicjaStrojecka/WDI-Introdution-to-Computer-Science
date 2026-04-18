# Zadanie 222.
# Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
# których klucz występuje dokładnie k razy. Do funkcji należy przekazać
# wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
# zwrócić informację czy usunięto jakieś elementy z listy.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def main(cycle, k:int) -> tuple:
    head = cycle
    counter = cycle
    dict = {}
    while True:
        dict[counter.val] = dict.get(counter.val, 0) + 1
        counter = counter.next
        if counter is head:
            break

    if all(dict[key] == k for key in dict):
        return True, None

    if all(dict[key] != k for key in dict):
        return False, cycle

    curr = head
    while True:
        if dict[curr.next.val] != k:
            head = curr.next
            break

    prev, curr = head, head.next
    while True:
        if dict[curr.val] == k:
            prev.next = curr.next
            curr = curr.next
        else:
            prev, curr = curr, curr.next

        if curr == head:
            return True, head