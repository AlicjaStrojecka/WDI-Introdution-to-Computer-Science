#Zadanie 19.
#iloczyn √0.5 ∗ (√ 0.5 + 0.5 ∗ √ 0.5) ∗ (√ 0.5 + 0.5 ∗ (√ 0.5 + 0.5 ∗ √ 0.5)) ∗ ...
#ma wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.

def half()->float:
    prev = result = (0.5) ** (1/2)
    backup = 0
    while result != backup:
        backup = result
        prev = (0.5 + (0.5 * prev)) ** (1/2)
        result *=prev
        print(result)
    return (2/result)

print(half())