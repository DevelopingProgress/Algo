def Policz(slowo):
    wynik = 1
    for znak in slowo:
        if znak.isalpha():
            wynik *= (ord(znak.lower()) - ord('a') + 1)
    return wynik


def Grupuj(wyrazy):
    slownik = {}
    for wyraz in wyrazy:
        hash = Policz(wyraz)
        if hash not in slownik.keys():
            lista = [wyraz]
            slownik[hash] = lista
        else:
            slownik[hash].append(wyraz)
    return slownik


dane = ["bca", "abc", "dca", "dcb"]
wynik = Grupuj(dane)

grupa = 0
for hash, lista in wynik.items():
    print("Grupa ", grupa, end=": ")
    for wyraz in lista:
        print(wyraz, end=" ")
    print()
    grupa += 1
