def czyPalindrom(x):
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n - 1):
        if x[i] != x[n - 1 - i]:
            return False
    return True


print("Program sprawdzajacy czy slowo jest palindromem")
print("Podaj slowo")
s1 = input()
print("Podane slowo " + ("jest " if (czyPalindrom(s1)) else "nie jest ") + "palindromem")
