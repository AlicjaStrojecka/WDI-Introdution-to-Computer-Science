#Zadanie 33.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na
#pytanie, czy jej cyfry stanowią ciąg rosnący.

def check(number:int)->bool:
    prev = number % 10
    for i in range (1, len(str(number))-1):
        next = (number % 10**(i+1)) // 10**(i)
        if prev <= next:
            return False
        prev = next
    return True
print(check(12355))
