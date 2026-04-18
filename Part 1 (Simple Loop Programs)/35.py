#Zadanie 35.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
#czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.

def check(number:int)->bool:
    lenght = len(str(number))
    for i in range(1, lenght+1):
        curr = (number % 10**(i)) // (10**(i-1))
        if curr == lenght:
            return True
    return False

print(check(1239))