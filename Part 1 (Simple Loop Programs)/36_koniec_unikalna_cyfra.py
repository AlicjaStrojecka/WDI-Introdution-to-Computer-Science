#Zadanie 36.
#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
#czy liczba ta zakończona jest unikalną cyfrą.

def check(number:int)->bool:
    unique = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(str(number))):
        curr = (number % 10**(i+1)) // (10**(i))
        if unique[curr] == 0:
            unique[curr] = 1
    if unique[number % 10] == 0:
        return True
    return False

print(check(12344))