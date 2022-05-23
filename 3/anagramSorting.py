def anagramCheck(str1, str2):
    # Convert string into lists
    list1 = list(str1)
    list2 = list(str2)
    # Sort the list value
    list1.sort()
    list2.sort()

    position = 0
    matches = True

    while position < len(str1) and matches:
        if list1[position] == list2[position]:
            position = position + 1
        else:
            matches = False

    return matches


print("Program sprawdzajacy czy dwa slowa sa anagramami")
print("Podaj pierwsze slowo")
s1 = input()
print("Podaj drugie slowo")
s2 = input()
print("Podane slowa " + ("sa " if (anagramCheck(s1, s2)) else "nie sa ") + "anagramami")
