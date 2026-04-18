# Zadanie 79.
# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą
# wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i
# dokładnie jeden element największy (liczba elementów najmniejszych oznacza liczbę takich
# elementów o tej samej wartości).

def main(T:list)->bool:
    highest = T[0]
    lowest = T[0]
    for number in T:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return T.count(highest) == 1 and T.count(lowest) == 1