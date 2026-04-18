#Zadanie 187. Wypisywanie elementów łańcucha

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def wypisz(p):
    while p != None:
        print(p.val)
        p = p.next

