#Zadanie 34.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na
#pytanie, czy jej cyfry stanowią ciąg geometryczny.

def check(number:int)->bool:
    prev = number % 10
    mid = number % 100 // 10
    q = mid / prev
    for i in range (2, len(str(number))-1):
        next = (number % 10**(i+1)) // 10**(i)
        if next/mid != q:
            return False
        mid = next
    return True

print(check(139))