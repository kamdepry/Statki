def podaj_kolumne():
    kolumny = "abcdefghij"
    while True:
        print("Podaj kolumnę.")
        kolumna = input()
        if kolumna in kolumny:
            break
        else:
            print("Nieprawidłowy znak. Wprowadź pierwszą współrzędną jeszcze raz.")
    return kolumna

def podaj_wiersz():
    while True:
        print("Podaj wiersz.")
        wiersz = int(input())
        if wiersz > 0 and wiersz < 11:
            break
        else:
            print("Nieprawidłowy znak. Podaj drugą współrzędną jeszcze raz.")
    return wiersz

podaj_kolumne()
podaj_wiersz()
