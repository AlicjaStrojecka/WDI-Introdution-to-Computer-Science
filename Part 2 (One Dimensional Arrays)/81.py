# Zadanie 81.
# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def is_palindrome(string:str)->bool:
    length = len(string) // 2
    return all(string[index] == string[-1-index] for index in range(length))

def main(table:list)->int:
    length = len(table)
    highest = 0
    for index in range(length):
        for size in range(length-index, 0, -1):
            palindrome = ""
            valid = True
            for next in range(index, index+size):
                if table[next] % 2 == 0:
                    valid = False
                    break
                palindrome += str(table[next])
            if not valid:
                continue
            if is_palindrome(palindrome):
               if highest < size:
                   highest = size
                break
    return highest


