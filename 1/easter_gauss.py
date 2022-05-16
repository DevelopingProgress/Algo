# Python3 program for the
# above approach
import math


def gaussEaster(Y):
    A = Y % 19
    B = Y % 4
    C = Y % 7
    P = math.floor(Y / 100)
    Q = math.floor((13 + 8 * P) / 25)
    M = (15 - Q + P - P // 4) % 30
    N = (4 + P - P // 4) % 7
    D = (19 * A + M) % 30
    E = (2 * B + 4 * C + 6 * D + N) % 7
    days = (22 + D + E)

    if (D == 29) and (E == 6):
        print(str(Y) + "-04-19")
        return

    elif (D == 28) and (E == 6):
        print(str(Y) + "-04-18")
        return

    else:
        if days > 31:
            print(str(Y) + "-04-" + str(days - 31))
            return
        else:
            print(Y + "-03-" + str(days))
            return


Y = 2023

gaussEaster(Y)
