# Zadanie 82.
# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów
# jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić długość znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def is_inc(string:str)->bool:
    length = len(string)
    return all(string[index] < string[index+1] for index in range(length-1))

def main(table:list)->int:
    length = len(table)
    highest = 0
    for index in range(length):
        for size in range(length-index, 0, -1):
            index_sum = 0
            element_sum = 0
            sequence = ""
            for next in range(index, index+size):
                index_sum += next
                element_sum += table[next]
                sequence += str(table[next])
                if is_inc(sequence):
                else:
                    sequence = ""
                    break
            if index_sum == element_sum:
                if highest < size:
                    highest = size
                    break
    return highest